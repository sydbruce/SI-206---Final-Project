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
    _id = response['city']['id']
    _city_name = response['city']['name']
    counter = 0
    for data in response['list']:
        _time = data['dt_txt']
        _temp_max = data['main']['temp_max']
        _temp_min = data['main']['temp_min']
        _humidity = data['main']['humidity']
        _weather_desc = data['weather'][0]['description']
        counter += 1
        if counter == 21:
            break
        cur.execute('INSERT OR IGNORE INTO WeatherData(id, city_name, time, temp_max, temp_min, humidity, weather_desc) VALUES (?,?,?,?,?,?,?)', (_id, _city_name, _time, _temp_max, _temp_min,  _humidity, _weather_desc))
        conn.commit()
    

LA = "5230092"
Weather_LA = getWeather(LA)
#getData(Weather_LA) running these commented out portions will populate the database, only run them once

Ann_Arbor = "4984247"
Weather_Ann_Arbor = getWeather(Ann_Arbor)
#getData(Weather_Ann_Arbor)

Detroit = "4990729"
Weather_Detroit = getWeather(Detroit)
#getData(Weather_Detroit)

Chicago = "3582383"
Weather_Chicago = getWeather(Chicago)
#getData(Weather_Chicago)

NYC = "5128638"
Weather_NYC = getWeather(NYC)
#getData(Weather_NYC)

