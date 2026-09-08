import urllib, base64

def url_encode(value):
    return urllib.parse.quote(value, safe='')

def base64_encode(value):
    return base64.b64encode(value.encode()).decode()