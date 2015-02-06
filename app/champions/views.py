from flask import render_template, json
from . import champions

# Twitch api: https://api.twitch.tv/kraken/streams
# Riot api: https://las.api.pvp.net/api/lol/static-data/las/v1.2/champion?locale=en_US&champData=all&api_key=RIOT_DEV_KEY

# Champ view - get the champions list from riot json
# and create a sorted list with it, display champ icon
# using Riot data dragon
@champions.route('/champion-streams')
def champ_index():
    with open('/tmp/riot_data.dat', 'r') as riot_data_file:
        # Add exception when the data file is empty or missing
        riot_data = json.loads(riot_data_file.read())
        champ_pool = sorted([champ for champ in riot_data['keys'].values()])

    return render_template('champions/champ_index.html',
                           champ_pool=champ_pool)

@champions.route('/champion/<champion>')
def single_champ(champion):
    return render_template('champions/champion_streams.html', champion=champion)
