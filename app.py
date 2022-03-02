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

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

#defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home():
    playerid = request.args.get('playerid')
    return render_template('home.html')

app.run(debug = True) 
