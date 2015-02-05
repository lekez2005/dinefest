__author__ = 'lekez2005'

import flask
from twilio import twiml
from flask import request
import os

app = flask.Flask(__name__)

@app.route('/call', methods=['POST'])
def call():
	response = twiml.Response()
	response.enqueue("Queue Demo", waitUrl="/wait")
	return str(response)

@app.route('wait', methods=['POST'])
def wait():
	response = twiml.Response()
	response.say(("You are number %s in the queue. Please hold." %
		request.form['QueuePosition']))
	return str(response)

if __name__=="__main__":
	port = int(os.environ.get('PORT', 5000))
	app.debug = True;
	app.run(host='0.0.0.0', port=port)
