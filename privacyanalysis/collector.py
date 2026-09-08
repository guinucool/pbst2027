from config import VALUES, NAMES, EXTRACTS, EMAIL_PARAM, VALUES_FILE, COLLECTED_FILE
from hashes import md5_hash, sha1_hash, sha256_hash
import re, urllib.parse, json, os

def assign_email_hash(email, findings, hash_dict):
    
    email_md5 = md5_hash(email)
    email_sha1 = sha1_hash(email)
    email_sha256 = sha256_hash(email)
    
    for name, finding in findings:
        
        if name == "hash" and finding not in [email_md5, email_sha1, email_sha256]:
            
            if finding not in hash_dict:
                
                hash_dict[finding] = []
                
            hash_dict[finding].append(email)
            
def check_hashes(findings, hash_dict):
    
    values = set()
    
    for name, finding in findings:
        
        if name != "hash" or (name == "hash" and (finding in hash_dict) and len(set(hash_dict[finding])) == 1 and len(hash_dict[finding]) > 1):
            
            values.add((name, finding))
            
    return values

def clean_findings(findings):
    
    cleaned = set()
    
    for name, finding in findings:
        
        for pattern in EXTRACTS:
            
            regex = re.search(pattern, finding)
            
            if regex:
                
                finding = regex.group(1)
                
        cleaned.add((name, finding))
            
    return cleaned

# Simple collection

def collect_value(value):
    
    findings = set()
    
    for name, pattern in VALUES.items():
        
        for find in re.findall(pattern, value):
            
            findings.add((name, find))
            
        for find in re.findall(pattern, urllib.parse.unquote(value)):
            
            findings.add((name, find))
            
    return findings

def collect_name(name, value):
    
    findings = set()
    
    for key, pattern in NAMES.items():
        
        if re.search(pattern, name):
            
            findings.add((key, value))
            
    return findings

def collect_value_and_name(name, value):
    
    return collect_value(value) | collect_name(name, value)

# Collection of requests

def collect_header(header):
    
    if header['name'] not in ['cookie', 'set-cookie', ':path']:
        
        findings = collect_value_and_name(header['name'], header['value'])
        
        return findings
    
    return set()

def collect_cookie(cookie):
    
    findings = collect_value_and_name(cookie['name'], cookie['value'])
        
    return findings

def collect_query(param):
    
    findings = collect_value_and_name(param['name'], param['value'])
        
    return findings

def collect_postdata(postdata):
    
    findings = collect_value(postdata['text'])
        
    return findings

def collect_request(request):
    
    findings = set()
    
    for header in request['headers']:
        
        findings |= collect_header(header)
        
    for cookie in request['cookies']:
        
        findings |= collect_cookie(cookie)
        
    for param in request['queryString']:
        
        findings |= collect_query(param)
        
    if 'postData' in request:
        
        findings |= collect_postdata(request['postData'])
        
    return findings

# 

def collect_har(har):
    
    findings = set()
    
    for entry in har['log']['entries']:
        
        findings |= collect_request(entry['request'])
        
    return findings

def collect_hars(root):
    
    findings = {}
    hash_dict = {}
    
    for path, _, files in os.walk(root):
        
        for file in files:
            
            if file.endswith('.har'):
                
                path_values = os.path.join(path, VALUES_FILE)
                path_collec = os.path.join(path, COLLECTED_FILE)
                path_har = os.path.join(path, file)
                
                with open(path_values, 'r') as f:
                    
                    content = f.read()
                    
                    regex = re.search(re.escape(EMAIL_PARAM) + r':(\S+)', content)
                    email = regex.group(1) if regex else "noemail"
                
                with open(path_har, 'r') as f:
                    
                    har = json.load(f)
                    findings[path_collec] = collect_har(har)
                    
                    assign_email_hash(email, findings[path_collec], hash_dict)
                    
                    
    for key, values in findings.items():
        
        cleaned = clean_findings(values)
        cleaned = check_hashes(cleaned, hash_dict)
        
        with open(key, 'w') as f:
            
            for name, value in cleaned:
                
                f.write(f"{name}:{value}\n")