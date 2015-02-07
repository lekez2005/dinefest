__author__ = 'lekez2005'

from models import User, Food, Locations
import itertools
import datetime

def add_user(number, menu = []):
	user = User(number = number, menu = menu)
	return user.save()

def pause_user(number):
	User.objects(number=number).active = False

def resume_user(number):
	User.objects(number=number).active = True

def list_user(number):
	user = User.objects(number=number).first()
	if user is not None:
		return user.menu

def remove_user(number):
	User.objects(number=number).delete()

def user_matches(user, date = datetime.date.today()):
	items = []
	menu = user.menu
	if menu is not None:
		for name in menu:
			words = name.strip().split()
			permutations = words
			if len(words) <= 3:
				permutations = itertools.permutations(words, len(words))
			for permute in permutations:
				phrase = '\"{0}\"'.format(' '.join(permute))
				foods = list(Food.objects(date=date).search_text(phrase))
				if foods:
					items.extend(foods)
		return list(frozenset(items))
	else:
		return items

def user_message(user, date=datetime.date.today()):
	matches = user_matches(user, date)
	ferris = []
	jj = []
	for match in matches:
		if match.location == Locations.JOHNJAY:
			nm = ' '.join(match.name.replace('John', '').replace('Jay', '').split())
			jj.append('{0} for {1}'.format(nm, match.time))
		else:
			ferris.append('{0} for {1}'.format(match.name, match.time))
	messg = ''
	if jj:
		messg += 'JohnJay: {0}'.format(', '.join(jj))
	if ferris:
		messg += ' Ferris: {0}'.format(', '.join(ferris))
	return messg