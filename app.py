__author__ = 'lekez2005'

import datetime
import flask
from twilio import twiml
from flask import request
from flask_debugtoolbar import DebugToolbarExtension
from models import User, Food, Meals
from flask_mongoengine import MongoEngine
import os

app = flask.Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'secretatdevfest'
app.config['MONGODB_SETTINGS'] = {'db': 'dining',
								  'host': 'mongodb://heroku_app33730521:md1uf7kadsu056tr9j13j62a0j@ds041581.mongolab.com:41581/heroku_app33730521'}
#app.config['DEBUG_TB_PANELS'] = [flask_mongoengine.pa]
toolbar = DebugToolbarExtension(app)

# mongoengine
db = MongoEngine()
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
	from scrape.fetch import fetch_day
	fetch_day(datetime.date(2015, 2, 4))
	return "Hey"

@app.route('/call', methods=['POST'])
def call():
	response = twiml.Response()
	response.enqueue("Queue Demo", waitUrl="/wait")
	return str(response)

@app.route('/wait', methods=['POST'])
def wait():
	response = twiml.Response()
	response.say(("You are number %s in the queue. Please hold." %
		request.form['QueuePosition']))
	return str(response)

if __name__=="__main__":
	port = int(os.environ.get('PORT', 5000))

	app.run(host='0.0.0.0', port=port)
