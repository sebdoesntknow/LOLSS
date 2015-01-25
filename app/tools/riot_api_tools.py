import requests

def query_riot_api(term):
    riot_api = "https://api.twitch.tv/kraken/search/streams?q={}"
    url = riot_api.format(term)
    result = requests.get(url).json()
    return result
