from config import HASH_VALUES
from hashes import md5_hash, sha1_hash, sha256_hash
from encondings import url_encode, base64_encode

def fetch_values(text):
    
    values = set()
    
    for line in text.splitlines():
        
        name, value = line.split(':')
        values.add((name, value))
    
    return values

def transform_values(values):
    
    transformed = set()
    
    for name, value in values:
        
        if name in HASH_VALUES:
            
            transformed.add((name, md5_hash(value)))
            transformed.add((name, sha1_hash(value)))
            transformed.add((name, sha256_hash(value)))
            
        transformed.add((name, url_encode(value)))
        transformed.add((name, base64_encode(value)))
    
    return transformed