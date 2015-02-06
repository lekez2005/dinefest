__author__ = 'lekez2005'

import unittest
import requests
from scrape import urls
from scrape.urls import JohnJay, Ferris, Meals
import datetime

class TestWeek(unittest.TestCase):
	def test_week3(self):
		week3 = datetime.date(2015, 2, 5)
		self.assertEqual(3, urls.getweek(week3))

	def test_week_sunday(self):
		week4 = datetime.date(2015, 2, 8)
		self.assertEqual(4, urls.getweek(week4))

	def test_week_sat(self):
		# check a Saturday
		sat = datetime.date(2015, 2, 7)
		self.assertEqual(3, urls.getweek(sat))

class TestDateNumber(unittest.TestCase):

	def test_date_singledigit(self):
		feb8 = datetime.date(2015, 2, 8)
		self.assertEqual('28', urls.date_number(feb8))

	def test_doubledigits(self):
		nov21 = datetime.date(2015, 11, 21)
		self.assertEqual('1121', urls.date_number(nov21))

class TestJohnJayUrl(unittest.TestCase):

	def test_FridayIsNone(self):
		friday = datetime.date(2015, 2, 6)
		self.assertIsNone(JohnJay.get_url(friday, None))

	def test_FridayIsNone(self):
		saturday = datetime.date(2015, 2, 7)
		self.assertIsNone(JohnJay.get_url(saturday, None))

	def testBreakfastIsNone(self):
		self.assertIsNone(JohnJay.get_url(datetime.date.today(), Meals.BREAKFAST))

	def testDate(self):
		date = datetime.date(2015, 2, 5)
		self.assertEqual('http://dining.columbia.edu/25week-threethursdaybrunch-john-jay',
						 JohnJay.get_url(date, Meals.BRUNCH))

	def testFullWeek(self):
		start_date = datetime.date(2015, 2, 1)
		for i in xrange(0, 6):
			date = start_date + datetime.timedelta(days=i)
			for meal in [Meals.BRUNCH, Meals.DINNER]:
				url = JohnJay.get_url(date, meal)
				if url is not None:
					print url
					r = requests.get(url)
					self.assertEqual(r.status_code, 200)

class TestFerrisUrl(unittest.TestCase):

	def test_SundayIsNone(self):
		friday = datetime.date(2015, 2, 8)
		self.assertIsNone(Ferris.get_url(friday, None))

	def testBrunchIsNone(self):
		friday = datetime.date(2015, 2, 8)
		self.assertIsNone(Ferris.get_url(friday, None))


	def testDate(self):
		date = datetime.date(2015, 2, 5)
		self.assertEqual('http://dining.columbia.edu/25week-three-thursday-lunch-fbc',
						 Ferris.get_url(date, Meals.LUNCH))

	def testFullWeek(self):
		start_date = datetime.date(2015, 2, 3)
		for i in xrange(0, 6):
			date = start_date + datetime.timedelta(days=i)
			for meal in [Meals.BREAKFAST, Meals.LUNCH, Meals.DINNER]:
				url = Ferris.get_url(date, meal)
				if url is not None:
					print url
					r = requests.get(url)
					self.assertEqual(r.status_code, 200)