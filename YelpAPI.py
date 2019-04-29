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



def setupYelpDataBase(YelpList):
    conn = sqlite3.connect('YelpData.sqlite')
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
def getCalculations(YelpData, city):
    conn = sqlite3.connect('YelpData.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT rating from YelpData WHERE city=" + city)
    for row in cur:
        rating = row[0][0:20]
        city[rating] = city.get(rating, 0) = 1


data1 = getYelp(YelpAPIKey, "Atlanta")
data2 = getYelp(YelpAPIKey, "Boston")
data3 = getYelp(YelpAPIKey, "Chicago")
data4 = getYelp(YelpAPIKey, "Detroit")
data5 = getYelp(YelpAPIKey, "Houston")
data6 = getYelp(YelpAPIKey, "Los Angeles")
data7 = getYelp(YelpAPIKey, "New York City")
data8 = getYelp(YelpAPIKey, "Philadelphia")
data9 = getYelp(YelpAPIKey, "San Francisco")
data10 = getYelp(YelpAPIKey, "Seattle")
setupYelpDataBase(data1)
setupYelpDataBase(data2)
setupYelpDataBase(data3)
setupYelpDataBase(data4)
setupYelpDataBase(data5)
setupYelpDataBase(data6)
setupYelpDataBase(data7)
setupYelpDataBase(data8)
setupYelpDataBase(data9)
setupYelpDataBase(data10)

AtlantaData = getCalculations('Atlanta')
