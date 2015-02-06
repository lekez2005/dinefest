__author__ = 'lekez2005'

import requests
from bs4 import BeautifulSoup

def parse(url):
	r = requests.get(url)
	if r.status_code == 200:
		html = r.content
		soup = BeautifulSoup(html, 'lxml')
		for meal in soup.find_all("div", class_="field-item"):
			pass
	else:
		return None


parse('http://dining.columbia.edu/25week-three-thursday-lunch-fbc')