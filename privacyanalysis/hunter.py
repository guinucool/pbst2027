from config import CONVERSATION_IDS, FIRSTPARTY
import urllib, zlib, re
import pandas as pd

def fetch_tp_domains(labelled):
    
    tp_domains = dict()
    
    for row in labelled.itertuples(index=False):
            
        llm = row.LLM
        domain = row.ThirdParty_Domain
        organization = row.Organization
        
        if llm not in tp_domains:
            
            tp_domains[llm] = dict()
        
        if organization != FIRSTPARTY:  
              
            tp_domains[llm][domain] = organization
            
    return tp_domains

# Value hunting

def regex_value(name, value):
    
    if (name in CONVERSATION_IDS):
        
        return rf'(?<!/)(?<!%2F){re.escape(value)}(?!/|%2F)'
    
    return rf'{re.escape(value)}'

def hunt_values(text, values):
    
    found_text = text
    found_values = []
    
    for name, value in values:
        
        regex = re.search(regex_value(name, value), text)

        if regex:
            
            found_values.append((name, value))
            found_text = re.sub(regex_value(name, value), f'<!{name} -> {value}>', found_text)
    
    return found_text, found_values

# Request hunting

def hunt_header(header, values):
    
    if header['name'] not in ['cookie', 'set-cookie', ':path']:
        
        found_text, matches = hunt_values(header['value'], values)
        
        return found_text, [('headers', name, value) for name, value in matches]
    
    return header['value'], []

def hunt_cookie(cookie, values):
    
    found_text, matches = hunt_values(cookie['value'], values)
    
    return found_text, [('cookies', name, value) for name, value in matches]

def hunt_query(param, values):
    
    found_text, matches = hunt_values(param['value'], values)
    
    return found_text, [('query', name, value) for name, value in matches]

def hunt_postdata(postdata, values):
    
    text = postdata['text']
    
    try:
        
        raw = text.encode('latin-1')
        text = zlib.decompress(raw)
        
    except:
        pass
    
    found_text, matches = hunt_values(text, values)
    
    return found_text, [('postdata', name, value) for name, value in matches]

def hunt_request(request, values):
    
    matches = []
    
    domain = urllib.parse.urlparse(request['url']).netloc
    path = urllib.parse.urlparse(request['url']).path
    
    for header in request['headers']:
        
        found_text, found_matches = hunt_header(header, values)
        
        header['value'] = found_text
        matches.extend([(domain, path, *match) for match in found_matches])
        
    for cookie in request['cookies']:
        
        found_text, found_matches = hunt_cookie(cookie, values)
        
        cookie['value'] = found_text
        matches.extend([(domain, path, *match) for match in found_matches])
        
    for param in request['queryString']:
        
        found_text, found_matches = hunt_query(param, values)
        
        param['value'] = found_text
        matches.extend([(domain, path, *match) for match in found_matches])
        
    if 'postData' in request:
        
        found_text, found_matches = hunt_postdata(request['postData'], values)
        
        request['postData']['text'] = found_text
        matches.extend([(domain, path, *match) for match in found_matches])
        
    return matches

# Hunt har

def hunt_har(har, tp_domains, values):
    
    matches = set()
    
    for entry in har['log']['entries']:
        
        request = entry['request']
        domain = urllib.parse.urlparse(request['url']).netloc
        
        if domain in tp_domains.keys():
            
            matches.update([(tp_domains[domain], *match) for match in hunt_request(request, values)])
            
    return matches