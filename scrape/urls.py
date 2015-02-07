__author__ = 'lekez2005'

import datetime
from models import Meals


BASE_URL = 'http://dining.columbia.edu/'
NUMBERS = {1: 'one', 2:'two', 3:'three', 4:'four', 5: 'five'}
DAYS = {0:'monday', 1:'tuesday', 2:'wednesday',
		3:'thursday', 4:'friday', 5:'saturday', 6: 'sunday', }


class JohnJay:

	@staticmethod
	def get_url(date, meal):
		weekday = date.weekday()
		if weekday in [4, 5]:
			return None
		if meal not in [Meals.BRUNCH, Meals.DINNER]:
			return None

		week = NUMBERS[getweek(date)]
		date_num = date_number(date)
		return '{base}{date_num}week-{week}{weekday}{meal}-john-jay'\
			.format(base=BASE_URL, date_num = date_num, week = week,
					weekday = DAYS[weekday], meal=meal)

class Ferris:

	@staticmethod
	def get_url(date, meal):
		weekday = date.weekday()
		if weekday == 6:
			return None
		if meal not in [Meals.BREAKFAST, Meals.LUNCH, Meals.DINNER]:
			return None

		week = NUMBERS[getweek(date)]
		date_num = date_number(date)
		return '{base}{date_num}week-{week}-{weekday}-{meal}-fbc'\
			.format(base=BASE_URL, date_num = date_num, week = week,
					weekday = DAYS[weekday], meal=meal)


def date_number(date):
	'''28 for Feb 8, 121 for Jan 21 '''
	month = date.month
	day = date.day
	return str(month)+str(day)

def getweek(date):
	# for 2015, subtract 17 days
	date_offset = date - datetime.timedelta(days=18)
	return 1 + date_offset.timetuple().tm_yday/7
