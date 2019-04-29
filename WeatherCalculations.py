import sqlite3
import matplotlib
import matplotlib.pyplot as plt


def get_precipitation_counts(db_filename, city_name):
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()
    dicts = {}
    cur.execute("SELECT weather_desc FROM WeatherData WHERE city_name = " + city_name)
    for row in cur:
        weather = (row[0][0:20])
        city_name[weather] = city_name.get(weather, 0) + 1
    
    return dicts

def visualize(d):
    xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "LA", "NYC", "Philadelphia", "San_Francisco", "Seattle"] 
    yvals = [d["Atlanta"], d["Boston"], d["Chicago"], d["Detroit"], d["Houston"], d["LA"], d["NYC"], d["Philadelphia"], d["San_Francisco"], d["Seattle"]]
    plt.bar(xvals, yvals, align = "center", color = ["red", "orange", "yellow", "green", "blue", "purple", "black", "brown", ""])
    plt.ylabel("Number of Tweets")
    plt.xlabel("Day tweeted")
    plt.title("Number of Tweets per Weekday")
    plt.show()
    plt.savefig("Canvas Upload")

AtlantaData = get_precipitation_counts("WeatherData.sql", city_name = "'Atlanta'")


print(AtlantaData)