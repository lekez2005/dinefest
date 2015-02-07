__author__ = 'lekez2005'

from flask import Blueprint, request, redirect
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from twilio import twiml
from models import User, Locations
from availability import building_open, density
from scrape import next_day
import datetime
import users

sms = Blueprint('sms', __name__)

account_sid = 'ACc4d5b57e194101318a808d72529944f3'
auth_token = 'd01bf01e211a03786eaccee21bcefa5f'

client = TwilioRestClient(account_sid, auth_token)

@sms.route('/sms',  methods=['POST'])
def receive_sms():
	from_number = request.values.get('From', None)
	body = request.values.get('Body', '')
	body = body.lower()
	resp = twiml.Response()

	if body.startswith('info'):
		resp.message("Commands: add <>, remove <>, list, today, tomorrow, pause, resume, stop, open")
	elif body.startswith('pause'):
		user = User.objects(number=from_number).first()
		if user:
			user.active = False
			user.save()
			resp.message("Paused, text resume to resume")
		else:
			resp.message("Not registered, to start, add an item to your list")
	elif body.startswith('resume'):
		user = User.objects(number=from_number).first()
		if user:
			user.active = True
			user.save()
			resp.message("Resumed, you will now get alerts")
		else:
			resp.message("Not registered, to start, add an item to your list")
	elif body.startswith('stop'):
		user = User.objects(number=from_number).first()
		if user:
			user.delete()
			resp.message("You are now unsubscribed")
		else:
			resp.message("Not registered, to start, add an item to your list")
	elif body.startswith('list'):
		user = User.objects(number=from_number).first()
		if user and user.menu:
			resp.message(' ,'.join(user.menu))
		elif user:
			resp.message('List empty, use add to add to list')
		else:
			resp.message("Not registered, to start, add an item to your list")
	elif body.startswith('add'):
		user = User.objects(number=from_number).first()
		item = body.split('add', 1)[1]
		if user:
			if len(user.menu) > 10:
					resp.message("Limit exceeded, please remove an item first")
			elif item.strip().lower() not in user.menu:
				user.menu.append(item.strip().lower())
				user.save()
				resp.message("Added " + item)
			else:
				resp.message("List already contained " + item)
		else:
			user = User(number=from_number, menu=[item]).save()
			resp.message("Welcome to dinefest!! Current list: {0}".format(', '.join(user.menu)))
	elif body.startswith('remove'):
		user = User.objects(number=from_number).first()
		item = body.split('remove', 1)[1]
		if user:
			if item.strip().lower() in user.menu:
				user.menu.remove(item.strip().lower())
				user.save()
				resp.message("removed {0}".format(item))
			else:
				resp.message("{0} not in list ".format(item))
		else:
			resp.message(resp.message("Not registered, to start, add an item to your list"))
	elif body.startswith('today'):
		user = User.objects(number=from_number).first()
		if user:
			messg = users.user_message(user, datetime.date.today())
			if not messg:
				resp.message("No match for today")
			else:
				resp.message(messg)
		else:
			resp.message(resp.message("Not registered, to start, add an item to your list"))
	elif body.startswith('tomorrow'):
		user = User.objects(number=from_number).first()
		if user:
			messg = users.user_message(user, datetime.date.today()+datetime.timedelta(days=1))
			if not messg:
				resp.message("No match for tomorrow")
			else:
				resp.message(messg)
		else:
			resp.message(resp.message("Not registered, to start, add an item to your list"))
	elif body.startswith('check'):
		item = body.split('check', 1)[1]
		user = User(number=from_number, menu=[item])
		messg = users.user_message(user, datetime.date.today())
		if not messg:
			resp.message("No match for today")
		else:
				resp.message(messg)
	elif body.startswith('open'):
		messg = ''
		if building_open.johnjay_open():
			messg += "JohnJay: {} \%".format(density.check_johnjay())
		if building_open.ferris_open(datetime.datetime.now()-datetime.timedelta(hours=5)):
			messg += "Ferris: {}\%".format(density.check_ferris())
		if messg:
			resp.message(messg)
		else:
			resp.message("No building open")
	elif body.startswith('next'):
		item = body.split('next', 1)[1]
		messg = ''
		if item:
			messg = next_day.find_next(item)
		if messg is None or not messg:
			resp.message('No {0} anytime soon'.format(item))
		else:
			resp.message(messg)
	else:
		resp.message('Commands: add <>, remove <>, list, today, tomorrow, pause, resume, stop, open')

	return str(resp)
	#send_message("+18565535260", "Hey there")

@sms.route('/sms/send_alerts', methods=['GET'])
def send_alerts():
	for user in User.objects(active=True):
		msg = users.user_message(user, datetime.date.today())
		if msg:
			send_message(user.number, msg)
	return 'Success'


def send_message(to, message):
	try:
		client.messages.create(to=to, from_="+12545346464", body=message)
	except TwilioRestException, e:
		print e