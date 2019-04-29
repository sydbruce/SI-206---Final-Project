
import requests
import json
import Keys
import sqlite3
import matplotlib
import matplotlib.pyplot as plt

zomato_key = Keys.ZomatoAPI
filename = 'ZomatoCalc.txt'

def getZomato(zomato_key, location):
        url = "https://developers.zomato.com/api/v2.1/locations"
        header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user-key": zomato_key}
        params = {'query': location}
        req = requests.get(url,params = params, headers=header)
        r = json.loads(req.text)
        return (r["location_suggestions"][0]["entity_id"], r["location_suggestions"][0]["entity_type"])


def getLocationDetails(zomato_key, city_input):
        city = getZomato(zomato_key, city_input)
        url = "https://developers.zomato.com/api/v2.1/location_details"
        header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user-key": zomato_key}
        params = {'entity_id': city[0], 'entity_type': city[1]}
        req = requests.get(url,params = params, headers=header)
        return json.loads(req.text)
        
        
def setupZomatoDataBase(data, cityName):
    conn = sqlite3.connect('CombinedDatabase.sqlite')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS ZomatoData(city_name TEXT, popularity TEXT, nightlife_index TEXT, best_rated_restaurant_name TEXT, best_rated_restaurant_price_range INTEGER, best_rated_restaurant_aggregate_rating TEXT)')
    
    for i in range(10):
            _city_name = data['location']['city_name']
            _popularity = data['popularity']
            _nightlife_index = data['nightlife_index']
            _best_rated_restaurant_name = data['best_rated_restaurant'][i]['restaurant']['name']
            _best_rated_restaurant_price_range = data['best_rated_restaurant'][i]['restaurant']['price_range']
            _best_rated_restaurant_aggregate_rating = data['best_rated_restaurant'][i]['restaurant']['user_rating']['aggregate_rating']
           
            cur.execute('INSERT INTO ZomatoData(city_name, popularity, nightlife_index, best_rated_restaurant_name, best_rated_restaurant_price_range, best_rated_restaurant_aggregate_rating) VALUES (?,?,?,?,?,?)', (_city_name, _popularity, _nightlife_index, _best_rated_restaurant_name, _best_rated_restaurant_price_range, _best_rated_restaurant_aggregate_rating))
            conn.commit()
    
    #The Calculations are Below and added into a new database
    rate_total = 0
    price_total = 0
    count = 0
    rate_average = 0
    cur.execute('SELECT * FROM ZomatoData')
    for row in cur:
            city_name = row[0]
            if city_name == cityName:
                    rate_total += float(row[5])
                    price_total += float(row[4])
                    count += 1
    rate_average = rate_total/count
    price_average = price_total/count

    
    

    conn = sqlite3.connect('ZomatoCalc.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ZomatoCalc(average_rate INTEGER, average_price INTEGER)')
    cur.execute('INSERT INTO ZomatoCalc(average_rate, average_price) VALUES (?,?)', (rate_average, price_average,))
    conn.commit()

    cur.execute('SELECT * FROM ZomatoCalc')
    counter = 0
    f = open(filename, 'w')
    for row in cur:
            counter += 1
            f.write("Restaurant Rating for restaurant " + str(counter) + " is: " + str(row[0]) + " and the Price Range is: " + str(row[1])+ "\n")



    

def createVisualizations():
        conn = sqlite3.connect('CombinedDatabase.sqlite')
        cur = conn.cursor()
        
        #Popularity Visualization
        popularity_dict = {}
        cur.execute("SELECT * from ZomatoData")
        for row in cur:
                if row[0] not in popularity_dict:
                        popularity_dict[row[0]] = float(row[1])
        xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "Los Angeles", "New York City", "Philadelphia", "San Francisco", "Seattle"]
        yvals = [popularity_dict["Atlanta"],popularity_dict["Boston"],popularity_dict["Chicago"],popularity_dict["Detroit"],popularity_dict["Houston"],popularity_dict["Los Angeles"],popularity_dict["New York City"],popularity_dict["Philadelphia"],popularity_dict["San Francisco"],popularity_dict["Seattle"]]
        plt.bar(xvals, yvals, align = "center", color= ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "grey"])
        plt.ylabel("Popularity Rating")
        plt.xlabel("City Name")
        plt.title("Popularity Rating for U.S. Cities")
        plt.savefig("cityPopularities.png")
        plt.show()

        #NightLife Visualization
        nightlife_dict = {}
        cur.execute("SELECT * from ZomatoData")
        for row in cur:
                if row[0] not in nightlife_dict:
                        nightlife_dict[row[0]] = float(row[2])
        xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "Los Angeles", "New York City", "Philadelphia", "San Francisco", "Seattle"]
        yvals = [nightlife_dict["Atlanta"],nightlife_dict["Boston"],nightlife_dict["Chicago"],nightlife_dict["Detroit"],nightlife_dict["Houston"],nightlife_dict["Los Angeles"],nightlife_dict["New York City"],nightlife_dict["Philadelphia"],nightlife_dict["San Francisco"],nightlife_dict["Seattle"]]
        plt.bar(xvals, yvals, align = "center", color= ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "grey"])
        plt.ylabel("Nightlife Rating")
        plt.xlabel("City Name")
        plt.title("Nightlife Rating for U.S. Cities")
        plt.savefig("cityNightlife.png")
        plt.show()

        conn = sqlite3.connect('ZomatoCalc.sqlite')
        cur = conn.cursor()
        
        #Restaurant Rating Visualization
        rate_list = []
        cur.execute("SELECT * from ZomatoCalc")
        for row in cur:
                rate_list.append(float(row[0]))
        xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "Los Angeles", "New York City", "Philadelphia", "San Francisco", "Seattle"]
        yvals = [rate_list[0],rate_list[1],rate_list[2],rate_list[3],rate_list[4],rate_list[5],rate_list[6],rate_list[7],rate_list[8],rate_list[9]]
        plt.bar(xvals, yvals, align = "center", color= ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "grey"])
        plt.ylabel("Restaurant Average Rating")
        plt.xlabel("City Name")
        plt.title("Restaurant Average Rating for U.S. Cities")
        plt.savefig("cityRestaurantRates.png")
        plt.show()

        #Restaurant Price Visualization
        price_list = []
        cur.execute("SELECT * from ZomatoCalc") #could have also just selcted price_average column w/out for loop
        for row in cur:
                price_list.append(float(row[1]))
        xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "Los Angeles", "New York City", "Philadelphia", "San Francisco", "Seattle"]
        yvals = [price_list[0],price_list[1],price_list[2],price_list[3],price_list[4],price_list[5],price_list[6],price_list[7],price_list[8],price_list[9]]
        plt.bar(xvals, yvals, align = "center", color= ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "grey"])
        plt.ylabel("Restaurant Average Price")
        plt.xlabel("City Name")
        plt.title("Restaurant Average Price for U.S. Cities")
        plt.savefig("cityRestaurantPrices.png")
        plt.show()

#Function calls to get data into DB   
data1 = setupZomatoDataBase(getLocationDetails(zomato_key, "Atlanta"), "Atlanta")
data2 = setupZomatoDataBase(getLocationDetails(zomato_key, "Boston"), "Boston")
data3 = setupZomatoDataBase(getLocationDetails(zomato_key, "Chicago"), "Chicago")
data4 = setupZomatoDataBase(getLocationDetails(zomato_key, "Detroit"), "Detroit")
data5 = setupZomatoDataBase(getLocationDetails(zomato_key, "Houston"), "Houston")
data6 = setupZomatoDataBase(getLocationDetails(zomato_key, "Los Angeles"), "Los Angeles")
data7 = setupZomatoDataBase(getLocationDetails(zomato_key, "New York City"), "New York City")
data8 = setupZomatoDataBase(getLocationDetails(zomato_key, "Philadelphia"), "Philadelphia")
data9 = setupZomatoDataBase(getLocationDetails(zomato_key, "San Francisco"), "San Francisco")
data10 = setupZomatoDataBase(getLocationDetails(zomato_key, "Seattle"), "Seattle")

#Function call to create Visualizations

visualize = createVisualizations()
f.close()

