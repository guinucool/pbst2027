from config import FP_DOMAINS, TP_DOMAIN_COLLECTOR, TP_DOMAIN_CLASSIFICATION, ACCOUNT, CHAT, PRIVACY, CONSENT, INTERACTION
import dns.resolver, tldextract, urllib.parse, os, re, json
import pandas as pd

def resolve_cname(domain):
    
    try:
        
        cname_records = dns.resolver.resolve(domain, 'CNAME')

        return cname_records[0].target.to_text(omit_final_dot=True)
    
    except (dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout):
        
        return ""
    
def is_first_party(domain, fp_domains):
    
    extracted = tldextract.extract(domain)
    return any(extracted.domain == tldextract.extract(fp_domain).domain for fp_domain in fp_domains)

def set_to_dataframe(s, columns):

    l = list(s)
    l.sort()
    
    return pd.DataFrame(l, columns=columns)

def extract_har(har, fp_domains):
    
    tp_domains = set()
    
    for entry in har['log']['entries']:
        
        domain = urllib.parse.urlparse(entry['request']['url']).netloc
        cname = resolve_cname(domain)
        
        if not is_first_party(domain, fp_domains) and not is_first_party(cname, fp_domains):
            
            tp_domains.add((domain, cname))
    
    return tp_domains

def extract_all(root):
    
    tp_collector = set()
    tp_classification = set()
    
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
                
                har_path = os.path.join(path, file)
                
                with open(har_path, 'r') as file:
                    
                    har = json.load(file)
                    
                    tp_domains = extract_har(har, FP_DOMAINS[llm])
                    
                    tp_collector.update((llm, ", ".join(FP_DOMAINS[llm]), domain, cname, ACCOUNT[account], CHAT[chat], PRIVACY[privacy], CONSENT[consent], INTERACTION[interaction]) for domain, cname in tp_domains)
                    tp_classification.update((llm, domain, cname) for domain, cname in tp_domains)
                    
    return set_to_dataframe(tp_collector, TP_DOMAIN_COLLECTOR), set_to_dataframe(tp_classification, TP_DOMAIN_CLASSIFICATION)