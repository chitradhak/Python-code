import requests
import json

def requestmod():
	urlreq = requests.get("https://toibnews.timesofindia.indiatimes.com/manageads/47191571.jsons?40")
	x = urlreq.response
	print x

requestmod()
