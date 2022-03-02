from flask import Flask
from flask import request
from flask import Markup
from flask import Flask
from flask import render_template
from datetime import datetime
from datetime import timedelta
import sqlite3
import logging
import numpy as np
import requests
from urllib.request import urlopen
import json

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

#defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home():
    playerid = request.args.get('playerid')
    season = request.args.get('season')
    player_points = return_player_points(playerid, season)
    timestamps = []
    points = []
    for match in player_points:
        timestamps.append(match)
        points.append(str(player_points[match]))
    timestamps = timestamps[::-1]
    points = points[::-1]
    timestamps = ','.join(timestamps)
    points = ','.join(points)
    return render_template('home.html', timestamps=timestamps, points=points, season=season, player_name=playerid)

def return_player_points(playerid, season):
    player_points_for_season = {}
    url = f"https://cnc-stats-api.azurewebsites.net/api/Player/{playerid}/Matches?season={season}"
    print(url)
    match_history = urlopen(url)
    match_history_json = json.loads(match_history.read())
    for match in match_history_json:
        match_start_time = match['starttime'].split(".")[0]
        dt_object = datetime.strptime(match_start_time, "%Y-%m-%dT%H:%M:%S")
        match_timestamp = datetime.timestamp(dt_object)*1000
        player_points = match['playerPoints']
        player_points_for_season[str(int(match_timestamp))] = player_points
    return player_points_for_season

def return_player_name(playerid):
    url = f"https://cnc-stats-api.azurewebsites.net/api/Player/{playerid}"
    match_history = urlopen(url)
    match_history_json = json.loads(match_history.read())
    return match_history_json['position']['name']

app.run(debug = True) 
