from weather import Weather
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

def getWeatherReport(query):
	weather = Weather()
	location = weather.lookup_by_location(query)
	if location is not None:
		condition = location.condition()
		print(condition.text())

		forecast = location.forecast()[0]

		weatherReport = "Today weather is {}\n Highest Tempreature is {}\n and Lowest Temprature is {}"
		return (weatherReport.format(forecast.text(), forecast.high(), forecast.low()))
	else:
		speak.Speak("Sorry, unable to find you location weather")