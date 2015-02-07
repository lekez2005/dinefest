__author__ = 'lekez2005'

from bs4 import BeautifulSoup

def parse(html):
	soup = BeautifulSoup(html, 'lxml')
	meals = []
	for meal in soup.find_all("div", class_="field-item"):
		name = meal.find("div", class_="meal-title").text
		link = None
		if meal.find('a') is not None:
			link = meal.find('a').get('href')
		meals.append({'name': name, 'link': link})
	return meals


#a = parse('http://dining.columbia.edu/25week-three-thursday-lunch-fbc')
#for meal in a:
#	print meal
