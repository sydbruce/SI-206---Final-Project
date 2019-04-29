import requests
import json
import Keys
import sqlite3
import pprint

def getWeather(city_id):
    api_key = Keys.api_key
    base_url = "http://api.openweathermap.org/data/2.5/forecast?id=" 
    complete_url = base_url + city_id + "&appid=" + api_key
    raw_response = requests.get(complete_url)
    response = raw_response.json()
    return response


def getData(response):
    conn = sqlite3.connect("WeatherData.sqlite") #Faulty, please read comments below
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS WeatherData(id TEXT UNIQUE, city_name TEXT, time TEXT,  temp_max INTEGER, temp_min INTEGER, humidity INTEGER, weather_desc TEXT)")
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
        if counter == 17:
            break
        cur.execute('INSERT OR IGNORE INTO WeatherData(id, city_name, time, temp_max, temp_min, humidity, weather_desc) VALUES (?,?,?,?,?,?,?)', (_id, _city_name, _time, _temp_max, _temp_min,  _humidity, _weather_desc))
        conn.commit()
    
#UNFIXABLE bug, database will no longer populate normally, as
#my data has already been successfully collected more than 1 week ago 
#The code has not changed, but the database will only populate one entry for each city 
#(Total of 10 entries, but is supposed to be 160)
#I will use the previously "healthy" database called "WeatherDataCorrect.sqlite" to create my visualizations
#Therefore, when YOU run these functions below, you will see a faulty sqlite database file named "WeatherData.sqlite"


Atlanta = "4671576"
Weather_Atlanta = getWeather(Atlanta)
getData(Weather_Atlanta)

Boston = "4930956"
Weather_Boston = getWeather(Boston)
getData(Weather_Boston)

Chicago = "3582383"
Weather_Chicago = getWeather(Chicago)
getData(Weather_Chicago)

Detroit = "4990729"
Weather_Detroit = getWeather(Detroit)
getData(Weather_Detroit)

Houston = "4699066"
Weather_Houston = getWeather(Houston)
getData(Weather_Houston)

LA = "3882428"
Weather_LA = getWeather(LA)
getData(Weather_LA) 

NYC = "5128638"
Weather_NYC = getWeather(NYC)
getData(Weather_NYC)

Philadelphia = "4560349"
Weather_Philadelphia = getWeather(Philadelphia)
getData(Weather_Philadelphia)

San_Francisco = "5391997"
Weather_San_Francisco = getWeather(San_Francisco)
getData(Weather_San_Francisco)

Seattle = "5809844"
Weather_Seattle = getWeather(Seattle)
getData(Weather_Seattle)
