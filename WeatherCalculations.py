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


def visualize():
    highs = [get_avg_high("CombinedDatabase.sqlite", city_name = "'Atlanta'")["'Atlanta'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'Boston'")["'Boston'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'Chicago'")["'Chicago'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'Detroit'")["'Detroit'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'Houston'")["'Houston'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'Los Angeles'")["'Los Angeles'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'New York'")["'New York'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'Philadelphia'")["'Philadelphia'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'San Francisco County'")["'San Francisco County'"], get_avg_high("CombinedDatabase.sqlite", city_name = "'Seattle'")["'Seattle'"]]
    lows = [get_avg_low("CombinedDatabase.sqlite", city_name = "'Atlanta'")["'Atlanta'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'Boston'")["'Boston'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'Chicago'")["'Chicago'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'Detroit'")["'Detroit'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'Houston'")["'Houston'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'Los Angeles'")["'Los Angeles'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'New York'")["'New York'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'Philadelphia'")["'Philadelphia'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'San Francisco County'")["'San Francisco County'"], get_avg_low("CombinedDatabase.sqlite", city_name = "'Seattle'")["'Seattle'"]]
    plt.scatter(highs, lows, color= ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "grey"])
    plt.ylabel("Temperature in Degrees Fahrenheit")
    plt.xlabel("City")
    plt.title("Average Low Temperature for Cities")
    plt.show()

    xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "LA", "NYC", "Philly", "SF", "Seattle"] 
    yvals = [get_humidity_avg("CombinedDatabase.sqlite", city_name = "'Atlanta'")["'Atlanta'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'Boston'")["'Boston'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'Chicago'")["'Chicago'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'Detroit'")["'Detroit'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'Houston'")["'Houston'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'Los Angeles'")["'Los Angeles'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'New York'")["'New York'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'Philadelphia'")["'Philadelphia'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'San Francisco County'")["'San Francisco County'"], get_humidity_avg("CombinedDatabase.sqlite", city_name = "'Seattle'")["'Seattle'"]]
    plt.bar(xvals, yvals, align = "center",  color = ["blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"])
    plt.ylabel("Humidity Percentage")
    plt.xlabel("City")
    plt.title("Average Humidity for Cities")
    plt.show()

visualize()




