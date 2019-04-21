import requests
import json
import Keys
import sqlite3
#pprint allows for the "prettified" printing of json paragraphs so that they can be read by humans
import pprint

#database configuration
def getWeather(city_id):
    api_key = Keys.api_key
    base_url = "http://api.openweathermap.org/data/2.5/forecast?id=" 
    complete_url = base_url + city_id + "&appid=" + api_key
    raw_response = requests.get(complete_url) 
    response = raw_response.json()
    #pprint.pprint(response) 
    return response

def getData(response):
    conn = sqlite3.connect("WeatherData.sql")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS WeatherData(id TEXT, city_name TEXT, time TEXT,  temp_max INTEGER, temp_min INTEGER, humidity INTEGER, weather_desc TEXT)")
    for data in response['city']:
        _id = data['coord']['id']
        print(_id)
        _city_name = data['name']
        _time = data['list'][0]['dt+text']
        _temp_max = data['list'][0]['main']['temp_max']
        _temp_min = data['list'][0]['main']['temp_min']
        _humidity = data['list'][0]['main']['humidity']
        _weather_desc = data['list'][0]['weather'][0]['description']
        cur.execute('INSERT OR IGNORE INTO WeatherData(id, city_name, time, temp_max, temp_min, humidity, weather_desc) VALUES (?,?,?,?,?,?,?)', (_id, _city_name, _time, _temp_max, _temp_min,  _humidity, _weather_desc))
        conn.commit()
       

LA = "5368381"
Weather_LA = getWeather(LA)
getData(Weather_LA)


Ann_Arbor = "4984247"
#Weather_Ann_Arbor = getWeather(Ann_Arbor)
#getData(Weather_Ann_Arbor)

Detroit = "4990729"
#Weather_Detroit = getWeather(Detroit)
#getData(Weather_Detroit)

