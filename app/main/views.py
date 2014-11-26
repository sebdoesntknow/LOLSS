from flask import Flask, render_template, current_app
from . import main

@main.route('/')
def index():
    twitch_api = 'https://api.twitch.tv/kraken/streams'
    return render_template('index.html')

