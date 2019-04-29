import sqlite3
import matplotlib
import matplotlib.pyplot as plt


def get_precipitation_counts(db_filename, city_name):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    city = {}
    cur.execute("SELECT weather_desc FROM WeatherData WHERE city_name = " + city_name)
    for row in cur:
        weather = (row[0][0:20])
        city[weather] = city.get(weather, 0) + 1
    
    return city

def get_humidity_avg(db_filename, city_name):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    city = {}
    sums = 0
    avg = 0
    cur.execute("SELECT humidity FROM WeatherData where city_name = " + city_name)
    for row in cur:
        humidity = row[0]
        sums += humidity
        avg = sums / 16
    city[city_name] = city.get(humidity, avg) 
    return city

def get_avg_high(db_filename, city_name):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    city = {}
    sums = 0
    avg = 0
    cur.execute("SELECT temp_max FROM WeatherData where city_name = " + city_name)
    for row in cur:
        temp_max = row[0]
        sums += temp_max
        avg = sums / 16
    city[city_name] = city.get(temp_max, avg * 9/5 - 459.67) 
    return city

def get_avg_low(db_filename, city_name):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    city = {}
    sums = 0
    avg = 0
    cur.execute("SELECT temp_min FROM WeatherData where city_name = " + city_name)
    for row in cur:
        temp_min = row[0]
        sums += temp_min
        avg = sums / 16
    city[city_name] = city.get(temp_min, avg * 9/5 - 459.67) 
    return city


def visualize(d):
    xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "LA", "NYC", "Philadelphia", "San_Francisco", "Seattle"] 
    yvals = [d["Atlanta"], d["Boston"], d["Chicago"], d["Detroit"], d["Houston"], d["LA"], d["NYC"], d["Philadelphia"], d["San_Francisco"], d["Seattle"]]
    plt.bar(xvals, yvals, align = "center", color = ["red", "orange", "yellow", "green", "blue", "purple", "black", "brown", "red", "orange"])
    plt.ylabel("Number of Tweets")
    plt.xlabel("Day tweeted")
    plt.title("Number of Tweets per Weekday")
    plt.show()
    plt.savefig("Canvas Upload")


#BostonData = get_precipitation_counts("WeatherData.sql", city_name = "'Boston'")
#ChicagoData = get_precipitation_counts("weatherData.sql", city_name = "'Chicago'")

AtlantaData = get_avg_low("WeatherData.sql", city_name = "'Atlanta'")
print(AtlantaData)
#print(BostonData)
#print(ChicagoData)