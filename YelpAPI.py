import requests
import json
import Keys
import sqlite3
import matplotlib
import matplotlib.pyplot as plt

Yelp_ClientID = Keys.client_ID
YelpAPIKey = Keys.API_Key

def getYelp(YelpAPIKey, search_city):
    headers = {'Authorization': 'Bearer %s' % YelpAPIKey}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'hotel', 'location': search_city}
    req = requests.get(url,params=params, headers=headers)
    print('The status code is {}'.format(req.status_code))
    return (json.loads(req.text))



def setupYelpDataBase(YelpList, city_name):
    conn = sqlite3.connect('WeatherDataCorrect.sqlite')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS YelpData(id TEXT UNIQUE, name TEXT, review_count INTEGER, rating FLOAT, price STRING, location TEXT, city TEXT)')
    counter = 0
    for yelp in YelpList['businesses']:
        _ID = yelp['id']
        _name = yelp['name']
        _review_count = yelp['review_count']
        _rating = yelp['rating']
        try:
            _price = yelp['price']
        except:
            _price = ' '
        _location = yelp['location']['address1']
        _city = yelp['location']['city']
        counter += 1
        if counter == 11:
            break

        cur.execute('INSERT OR IGNORE INTO YelpData(id, name, review_count, rating, price, location, city) VALUES (?,?,?,?,?,?,?)', (_ID, _name, _review_count, _rating, _price, _location, _city))
        conn.commit()

    #The Calculations are Below and added into a new database

    
    cur.execute("SELECT rating, city, price from YelpData")
    total = 0
    avg_price = 0
    count = 0
    for row in cur:
        city = row[1]
        price = len(row[2])
        if city == city_name:
            total += (row[0])
            avg_price += price
            count += 1
    average = total/count
    conn = sqlite3.connect('YelpCalc.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS YelpCalc(average INTEGER, avg_price INTEGER)')

    cur.execute('INSERT INTO YelpCalc(average, avg_price) VALUES (?,?)', (average,avg_price,))
    conn.commit()



def createYELPVisualizations():
        conn = sqlite3.connect('WeatherDataCorrect.sqlite')
        cur = conn.cursor()     

    #Vizualization for Average Hotel Rank
        avg_hotel_list = []
        cur.execute("SELECT * from YelpCalc")
        for row in cur:
            avg_hotel_list.append(float(row[0]))
        xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "Los Angeles", "New York", "Philadelphia", "San Francisco", "Seattle"]
        yvals = [avg_hotel_list[0],avg_hotel_list[1],avg_hotel_list[2],avg_hotel_list[3],avg_hotel_list[4],avg_hotel_list[5],avg_hotel_list[6],avg_hotel_list[7],avg_hotel_list[8],avg_hotel_list[9]]
        plt.bar(xvals, yvals, align = "center", color= ["red", "yellow", "orange", "green", "blue", "purple", "pink", "brown", "black", "grey"])
        plt.ylabel("Hotel Average Rating")
        plt.xlabel("City")
        plt.title("Hotel Average Rating for U.S. Cities")
        plt.savefig("cityHotelRates.png")
        plt.show()

    #Visualization for Total Price of Hotels per City
        totalprice = []
        cur.execute("SELECT * from YelpCalc")
        for row in cur:
            totalprice.append(int(row[1]))
        xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "Los Angeles", "New York", "Philadelphia", "San Francisco", "Seattle"]
        yvals = [totalprice[0],totalprice[1],totalprice[2],totalprice[3],totalprice[4],totalprice[5],totalprice[6],totalprice[7],totalprice[8],totalprice[9]]
        plt.bar(xvals, yvals, align = "center", color= ["red", "yellow", "orange", "green", "blue", "purple", "pink", "brown", "black", "grey"])
        plt.ylabel("Total Price of Top 10 Hotels (Number of $)")
        plt.xlabel("Cities")
        plt.title("Total Price of all Top 10 Hotels per City")
        plt.savefig("TotalPrice.png")
        plt.show()




#Function calls to get data into DB 
data1 = getYelp(YelpAPIKey, "Atlanta")
data2 = getYelp(YelpAPIKey, "Boston")
data3 = getYelp(YelpAPIKey, "Chicago")
data4 = getYelp(YelpAPIKey, "Detroit")
data5 = getYelp(YelpAPIKey, "Houston")
data6 = getYelp(YelpAPIKey, "Los Angeles")
data7 = getYelp(YelpAPIKey, "New York")
data8 = getYelp(YelpAPIKey, "Philadelphia")
data9 = getYelp(YelpAPIKey, "San Francisco")
data10 = getYelp(YelpAPIKey, "Seattle")
setupYelpDataBase(data1, 'Atlanta')
setupYelpDataBase(data2, 'Boston')
setupYelpDataBase(data3, 'Chicago')
setupYelpDataBase(data4, 'Detroit')
setupYelpDataBase(data5, 'Houston')
setupYelpDataBase(data6, 'Los Angeles')
setupYelpDataBase(data7, 'New York')
setupYelpDataBase(data8, 'Philadelphia')
setupYelpDataBase(data9, 'San Francisco')
setupYelpDataBase(data10, 'Seattle')

#Function call to create Visualizations
YelpVisualizations = createYELPVisualizations()
