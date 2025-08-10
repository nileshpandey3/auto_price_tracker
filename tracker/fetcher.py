import requests


def fetch_url(url):
    try:
        resp = requests.get(url)
        return resp.text
    except requests.HTTPError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
        raise
