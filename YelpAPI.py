import requests
import json
import Keys
import sqlite3

Yelp_ClientID = Keys.client_ID
YelpAPIKey = Keys.API_Key

def getYelp(YelpAPIKey):
    headers = {'Authorization': 'Bearer %s' % YelpAPIKey}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'food', 'location': 'Ann Arbor'}
    req = requests.get(url,params=params, headers=headers)
    print('The status code is {}'.format(req.status_code))
    YelpData = json.loads(req.text)


def setupYelpDataBase(YelpList):
    conn = sqlite3.connect('YelpData.sqlite')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS YelpData(name TEXT, review_count INTEGER, rating INTEGER, location TEXT')

    for yelp in YelpList:
        _name = yelp['name']
        _review_count = yelp['review_count']
        _rating = yelp['rating']
        _location = yelp['location'][0]

        cur.execute('INSERT INTO YelpData(name, review_count, rating, location) VALUES (?,?,?,?)', (_name, _review_count, _rating, _location))

    conn.commit()

data = getYelp(YelpAPIKey)           
database = setupYelpDataBase(data)
