import requests
import ipdb

def fetch_url(url):
    ipdb.set_trace()
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text
    


