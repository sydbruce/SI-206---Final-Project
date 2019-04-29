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
hi = """
def visualize(d):
    xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "LA", "NYC", "Philadelphia", "San_Francisco", "Seattle"] 
    yvals = [d["Atlanta"], d["Boston"], d["Chicago"], d["Detroit"], d["Houston"], d["LA"], d["NYC"], d["Philadelphia"], d["San_Francisco"], d["Seattle"]]
    plt.bar(xvals, yvals, align = "center", color = ["red", "orange", "yellow", "green", "blue", "purple", "black", "brown", ""])
    plt.ylabel("Number of Tweets")
    plt.xlabel("Day tweeted")
    plt.title("Number of Tweets per Weekday")
    plt.show()
    plt.savefig("Canvas Upload")
"""

AtlantaData = get_precipitation_counts("WeatherData.sql", city_name = "'Atlanta'")
BostonData = get_precipitation_counts("WeatherData.sql", city_name = "'Boston'")
ChicagoData = get_precipitation_counts("weatherData.sql", city_name = "'Chicago'")

print(AtlantaData)
print(BostonData)
print(ChicagoData)