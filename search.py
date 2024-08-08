import requests


def getUrl(query):
	url = "https://app.ticketmaster.com/discovery/v2/events.json?keyword="
	end = "&apikey=hYizuDEiKnFOmIx7EqQAOnOnbeGenc8h"
	return url + query + end


def getResults(query):
	response = requests.get(getUrl(query))
	data = response.json()
	return data