import requests


def website_is_up(url):
    try:
        requests.get(url)
        return True
    except requests.ConnectionError:
        return False
