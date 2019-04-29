import requests
import json
import Keys
import sqlite3

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
    conn = sqlite3.connect('CombinedDatabase.sqlite')
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

#gets average hotel ranking per city
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
        conn = sqlite3.connect('CombinedDatabase.sqlite')
        cur = conn.cursor()     
        cur.execute("SELECT * FROM YelpData")

        city_list = []
        for row in cur:
            city_list.append(average)




        xvals = ["Atlanta", "Boston", "Chicago", "Detroit", "Houston", "Los Angeles", "New York", "Philadelphia", "San Francisco", "Seattle"]


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


