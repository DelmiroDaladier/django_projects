import re

def check_url(url: str):
    regex = r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'
    return bool(re.search(regex, url))

def remove_http(url: str):
    return re.sub(r'^(http|https)://', '', url)