__author__ = 'lekez2005'

import requests
import unicodedata
from bs4 import BeautifulSoup

def find_next(food):
	url = "http://dining.columbia.edu/mood-search/js"
	r = requests.get(url, params={'meal_mood': food,
								  'form_build_id': 'form-f498101e6d81c5c3baaa1d906da47ec9',
								  'form_id': 'menu_mood_form',
								  'mood_search': 'Find'})
	if r.status_code == 200:
		content = unicode(r.content).decode('unicode-escape')
		soup = BeautifulSoup(content, 'lxml')
		try:
			first = soup.find('tr', class_='row odd').find_all('td', class_='mood-cell')
			name = first[0].text
			time_location = first[1].text
			return '{} at {}'.format(time_location, name)
		except Exception, e:
			print e
