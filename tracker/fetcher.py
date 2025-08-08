# First accept a url and a target price 
# Parse it
# request the current price 
# decide whether to notify or not

import requests
import ipdb

def fetch_url(url):
    resp = requests.get(url)
    with open(file='product_result.text',mode='w+') as f:
        f.write(resp.text)
    


