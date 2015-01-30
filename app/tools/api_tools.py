import os, requests

class ApiGetter(object):

    def __init__(self):

        # Riot Games API
        self.riot = "RITO PLS"
        # API Dev Key
        self.riot_dev_key = os.environ.get('RIOT_DEV_KEY')
        # Champions
        self.riot_champs = os.environ.get('RIOT_API_CHAMP_INFO')
        # Other data below

        # Twitch.tv API
        self.twitch = "Kaceytron lel"
        # API Search engine
        self.twitch_api = "https://api.twitch.tv/kraken/search/streams?q={}"

    def get_riot(self):
        pass

    def get_twitch(self, search):
        yield requests.get(self.twitch_api.format(search)).json()
