import requests
import json
import Keys
import sqlite3
import pprint

#database configuration
def SQLSetup():
    conn = sqlite3.connect("NutritionixData.sql")
    cur = conn.cursor()
    cur.execute("CREATE TABLE ")
    

api_key = Keys.api_key
base_url = "http://api.openweathermap.org/data/2.5/forecast?id="
city_id = input("Enter city id : ") 
complete_url = base_url + city_id + "&appid=" + api_key
raw_response = requests.get(complete_url) 
response = raw_response.json()

pprint.pprint(response)

LA = "5368381"
#if response["cod"] != "404": 
#	data = response["main"] 
#	current_temperature = data["temp"] 
#	current_pressure = data["pressure"] 
#	current_humidiy = data["humidity"] 
#	description = response["weather"] 
#	weather_description = description[0]["description"] 
#	print(" Temperature (in kelvin unit) = " +
#					str(current_temperature) +
#		"\n humidity (in percentage) = " +
#					str(current_humidiy) +
#		"\n description = " +
#					str(weather_description)) 

#else: 
#	print(" City Not Found ") 


