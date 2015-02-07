__author__ = 'lekez2005'

import datetime
import flask
from twilio import twiml
from flask import request
from flask_debugtoolbar import DebugToolbarExtension
from models import User, Food, Meals
from scrape import next_day
from flask_mongoengine import MongoEngine
import users
import os
from twil.sms import sms

app = flask.Flask(__name__)
app.register_blueprint(sms)

app.debug = True
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MONGODB_SETTINGS'] = {'db': 'dining',
								  'host': 'mongodb://heroku_app33730521:md1uf7kadsu056tr9j13j62a0j@ds041581.mongolab.com:41581/heroku_app33730521'}
#app.config['DEBUG_TB_PANELS'] = [flask_mongoengine.pa]
#toolbar = DebugToolbarExtension(app)

# mongoengine
db = MongoEngine()
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
	#u = users.user_matches(207333, datetime.date(2015, 2, 6))
	#users.add_user(207333, ['fried and rice', 'rice'])
	#from scrape.fetch import fetch_day
	#fetch.fetch_day(datetime.date(2015, 2, 8))
	next_day.find_next('rice')
	return "Hey"


if __name__=="__main__":
	port = int(os.environ.get('PORT', 5000))

	app.run(host='0.0.0.0', port=port)
