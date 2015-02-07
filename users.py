__author__ = 'lekez2005'

from models import User, Food
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

def user_matches(number, date = datetime.date.today()):
	items = []
	menu = list_user(number)
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
		for fo in items:
			print fo.name
		return list(frozenset(items))
	else:
		return items
