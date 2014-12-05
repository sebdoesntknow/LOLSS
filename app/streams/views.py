from flask import render_template, json
from . import streams

@streams.route('/')
def index():
    # Get the streams information from the twitch api
    # twitch_api = 'https://api.twitch.tv/kraken/streams'
    # Save the data to a variable, use .decode('utf-8')
    # to convert to string, and save to raw_data.dat
    lol_channels = []

    # Save the raw data to a file, then use json
    # to convert from str to object.
    with open('/tmp/raw_data.dat', 'r') as raw_data:
        twitch_api_raw_data = json.loads(raw_data.read())
        streams_data = twitch_api_raw_data['streams']

    for stream in streams_data:
        if 'League of Legends' in stream['channel']['game']:
            lol_channels.append(stream)

    return render_template('index.html', stream_list=lol_channels)

