# First accept a url and a target price 
# Parse it
# request the current price 
# decide whether to notify or not

import requests
import ipdb

def fetch_url(url):
    ipdb.set_trace()
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text
    


