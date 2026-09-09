from config import COLLECTED_FILE, CONVERSATION_IDS, FIRSTPARTY, FLAGGED_PREFIX, FLAGGED_SUFFIX, LEAKS, PRIVACY, VALUES_FILE, ACCOUNT, CHAT, CONSENT, INTERACTION
from values import fetch_values_from_file, transform_values
import urllib, zlib, re, os, json
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

# Search request text for known tracked values (e.g. IDs, emails)
# and redact them in place, recording which values were found and where.

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

# Apply value hunting across the different parts of an HTTP request
# (headers, cookies, query params, and POST body), redacting matches and
# tagging each finding with the domain, path, and location it came from.

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

# Walk HAR files (and their per-session metadata) on disk, flag any
# tracked values found in requests to known third-party domains, and
# collect matches labelled with the session's experimental configuration.

def hunt_har(har, tp_domains, values):
    
    matches = set()
    
    for entry in har['log']['entries']:
        
        request = entry['request']
        domain = urllib.parse.urlparse(request['url']).netloc
        
        if domain in tp_domains.keys():
            
            matches.update([(tp_domains[domain], *match) for match in hunt_request(request, values)])
            
    return matches

def hunt_hars(root, path_labelled):
    
    matches = set()
    
    for path, _, files in os.walk(root):
        
        for file in files:
            
            if file.endswith('.har'):
                
                regex = re.search(r'(\w+)-A(\d)-P(\d)-T(\d)-C(\d)-S\d-\d{8}/I(\d)', path)
                llm = regex.group(1)
                account = regex.group(2)
                chat = regex.group(3)
                privacy = regex.group(4)
                consent = regex.group(5)
                interaction = regex.group(6)
                
                path_info = os.path.join(path, VALUES_FILE)
                path_collected = os.path.join(path, COLLECTED_FILE)
                path_har = os.path.join(path, file)
                path_flagged = os.path.join(path, FLAGGED_PREFIX + file + FLAGGED_SUFFIX)
                
                values = fetch_values_from_file(path_info)
                values |= fetch_values_from_file(path_collected)
                values |= transform_values(values)
                
                tp_domains = fetch_tp_domains(pd.read_csv(path_labelled))
                
                with open(path_har, 'r') as file:
                    
                    har = json.load(file)
                    found_matches = hunt_har(har, tp_domains[llm], values)
                    
                    matches.update([(llm, *match, ACCOUNT[account], CHAT[chat], PRIVACY[privacy], CONSENT[consent], INTERACTION[interaction]) for match in found_matches])
                        
                    with open(path_flagged, 'w') as f:
                            
                        json.dump(har, f, indent=4)
                        
    matches = list(matches)
    matches.sort()
    
    return pd.DataFrame(matches, columns=LEAKS)