import requests
import json
import Keys
import sqlite3

Yelp_ClientID = Keys.client_ID
YelpAPIKey = Keys.API_Key

def getYelp(YelpAPIKey, search_city):
    headers = {'Authorization': 'Bearer %s' % YelpAPIKey}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'food', 'location': search_city}
    req = requests.get(url,params=params, headers=headers)
    print('The status code is {}'.format(req.status_code))
    return json.loads(req.text)



def setupYelpDataBase(YelpList):
    conn = sqlite3.connect('YelpData.sqlite')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS YelpData(id TEXT UNIQUE, name TEXT, review_count INTEGER, rating FLOAT, price STRING, location TEXT)')

    print(YelpList.keys())
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

        cur.execute('INSERT OR IGNORE INTO YelpData(id, name, review_count, rating, price, location) VALUES (?,?,?,?,?,?)', (_ID, _name, _review_count, _rating, _price, _location))
        conn.commit()
    

data = getYelp(YelpAPIKey, 'Ann Arbor')  
data2 = getYelp(YelpAPIKey, 'Los Angeles')         
setupYelpDataBase(data)
setupYelpDataBase(data2)
