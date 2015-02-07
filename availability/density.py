__author__ = 'lekez2005'

import requests, json

AUTH_TOKEN = '4SNFADGANV2JFMAB3UKCTWR7U7JAD2SN'

def check_johnjay():
	url = 'http://density.adicu.com/latest/group/{group_id}'.format(group_id=125)
	r = requests.get(url, params={'auth_token':AUTH_TOKEN})
	if r.status_code == 200:
		resp = json.loads(r.content)
		return resp['data'][0]['client_count']
	else:
		return None


def check_ferris():
	third_floor = 'http://density.adicu.com/latest/group/{group_id}'.format(group_id=152)
	fourth_floor = 'http://density.adicu.com/latest/group/{group_id}'.format(group_id=153)

	r = requests.get(third_floor, params={'auth_token':AUTH_TOKEN})
	third = -1
	fourth = -1
	if r.status_code == 200:
		resp = json.loads(r.content)
		third = resp['data'][0]['client_count']
	r = requests.get(fourth_floor, params={'auth_token':AUTH_TOKEN})
	if r.status_code == 200:
		resp = json.loads(r.content)
		fourth = resp['data'][0]['client_count']
	if third > 0 and fourth > 0:
		return int(0.75*third + 0.25*fourth)
	elif third > 0:
		return third
	elif fourth > 0:
		return fourth
	else:
		return None
