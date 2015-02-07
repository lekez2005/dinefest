__author__ = 'lekez2005'

from mongoengine import *

class User(Document):
	number = IntField(required=True)
	menu = ListField(field=StringField)
	active = BooleanField(default=True)


class Food(Document):
	name = StringField(required=True)
	date = DateTimeField(required=True)
	time = StringField(required=True)
	location = StringField(required=True)
	link = StringField()

	meta = {'indexes': [
			{'fields': ["$name", ]}
	]}

class Meals:
	BREAKFAST = 'breakfast'
	BRUNCH = 'brunch'
	LUNCH = 'lunch'
	DINNER = 'dinner'

class Locations:
	FERRIS = 'ferris'
	JOHNJAY = 'johnjay'