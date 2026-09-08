import hashlib

def md5_hash(value):
    return hashlib.md5(value.encode()).hexdigest()

def sha1_hash(value):
    return hashlib.sha1(value.encode()).hexdigest()

def sha256_hash(value):
    return hashlib.sha256(value.encode()).hexdigest()