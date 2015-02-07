__author__ = 'lekez2005'

from flask import Blueprint
from twilio.rest import TwilioRestClient
from twilio import twiml

sms = Blueprint('sms', __name__)

account_sid = 'ACc4d5b57e194101318a808d72529944f3'
auth_token = 'd01bf01e211a03786eaccee21bcefa5f'

client = TwilioRestClient(account_sid, auth_token)

@sms.route('/sms',  methods=['POST'])
def receive_sms():
	resp = twiml.Response()
	resp.message("Hey there")
	print resp
	return str(resp)
	#send_message("+18565535260", "Hey there")


def send_message(to, message):
	client.messages.create(to=to, from_="+12073447209", body=message)