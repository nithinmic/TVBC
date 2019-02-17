import requests

def weather_api(name):
	api="https://api.openweathermap.org/data/2.5/weather?appid=2012951d8cf61a1516d510cc4f741721&q="
	cityname=name
	url=api + cityname + "&units=metric"
	return requests.get(url).json()
	
