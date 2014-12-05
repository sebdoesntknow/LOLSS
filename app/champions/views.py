from flask import render_template, json
from . import champions

# Riot api: https://las.api.pvp.net/api/lol/static-data/las/v1.2/champion?locale=en_US&champData=all&api_key=RIOT_DEV_KEY

# Champ view - get the champions list from riot json
# and create a sorted list with it, display champ icon
# using Riot data dragon
@champions.route('/champion-streams')
def champ_index():
    return render_template('champions/champ_index.html')

@champions.route('/champion/<champion>')
def single_champ(champion):
    return render_template('champions/champion_streams.html', champion=champion)
