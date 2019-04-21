import requests
import json
import Keys
import sqlite3
#pprint allows for the "prettified" printing of json paragraphs so that they can be read by humans
import pprint

#database configuration
def SQLSetup():
    conn = sqlite3.connect("NutritionixData.sql")
    cur = conn.cursor()
    cur.execute("CREATE TABLE ")


def getWeather(city_id):
    api_key = Keys.api_key
    base_url = "http://api.openweathermap.org/data/2.5/forecast?id=" 
    complete_url = base_url + city_id + "&appid=" + api_key
    raw_response = requests.get(complete_url) 
    response = raw_response.json()
    pprint.pprint(response) 
    return None


LA = "5368381"
getWeather(LA)
Ann_Arbor = "4984247"
#getWeather(Ann Arbor)
