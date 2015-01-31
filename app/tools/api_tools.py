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

    # get_riot() needs a lot of improvement
    def get_riot(self, opt='champs', datafile='/tmp/riot_data.dat'):
        if opt == 'champs':
            resp = requests.get(self.riot_champs + self.riot_dev_key)
            with open(datafile, 'w') as dfile:
                dfile.write(resp.text)
                
        return 'Data saved to %r' % datafile

    def get_twitch(self, search):
        # Update to use generator instead
        return requests.get(self.twitch_api.format(search)).json()
