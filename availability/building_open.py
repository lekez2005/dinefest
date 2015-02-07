__author__ = 'lekez2005'

import datetime

def johnjay_open(time=datetime.datetime.now()):
	if time.weekday() in [4, 5]:
		return False
	elif time.weekday() == 6:
		if time.hour >=10 and time.hour <= 13:
			return True
		elif time.hour >=17 and time.hour <= 19:
			return True
		else:
			return False
	else:
		if time.hour >=11 and time.hour <= 13:
			return True
		elif time.hour >=17 and time.hour <= 19:
			return True
		else:
			return False

def ferris_open(time=datetime.datetime.now()):
	if time.weekday() == 6:
		return False
	elif time.weekday() == 5:
		if 9 <= time.hour <= 20:
			return True
		else:
			return False
	else:
		if 7 <= time.hour <= 20:
			return True
		else:
			return False