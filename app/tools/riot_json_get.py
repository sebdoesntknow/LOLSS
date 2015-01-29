#!/bin/env python
#
import os, urllib.request

def get_data(url, datafile):
    # urllib.request the riot raw data, store into variable
    # decode variable, from bytes to str (utf8)
    # save to file, load from there
    with open(datafile, 'w') as dfile:
        raw_data = urllib.request.urlopen(url)
        dfile.write(raw_data.read().decode('utf-8'))

# TODO: get twitch api data and store it somewhere.

riot_api_champs_url = os.environ.get('RIOT_API_CHAMP_INFO') + os.environ.get('RIOT_DEV_KEY')
twitch_api_url = os.environ.get('TWITCH_API_LOL')

get_data(riot_api_champs_url, "/tmp/riot_champs_data.dat")
get_data(twitch_api_url, "/tmp/twitch_data.dat")
