__author__ = 'lekez2005'

import datetime
from urls import Ferris, JohnJay
from models import Meals, Food, Locations
import requests
import parse


def update_john_jay(date):
	for meal in [Meals.BRUNCH, Meals.DINNER]:
		url = JohnJay.get_url(date, meal)
		if url is not None:
			add_to_db(url, meal, date, Locations.JOHNJAY)


def update_ferris(date):
	for meal in [Meals.BREAKFAST, Meals.LUNCH, Meals.DINNER]:
		url = Ferris.get_url(date, meal)
		if url is not None:
			add_to_db(url, meal, date, Locations.FERRIS)


def add_to_db(url, meal, date, location):
	r = requests.get(url)
	if r.status_code == 200:
		html = r.content
		meals = parse.parse(html)
		meals_db = []
		for food in meals:
			f = Food(name=food['name'], link=food['link'], location=location,
					 date=date, time=meal)
			meals_db.append(f)
		Food.objects.insert(meals_db)





def fetch_day(date=datetime.date.today()):
	update_ferris(date)
	update_john_jay(date)

