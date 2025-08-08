# First accept a url and a target price 
# Parse it
# request the current price 
# decide whether to notify or not

import requests

def fetch_url(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text
    


