
import requests
import json
import Keys
import sqlite3

zomato_key = Keys.ZomatoAPI
"""
url = "https://developers.zomato.com/api/v2.1/categories"

#Pull ids for categories
request = requests.get(url, headers={'user-key': zomato_key})
print(json.loads(request.text))


def find_cities(zomato_key, query):
    url = "https://developers.zomato.com/api/v2.1/cities"
    request = requests.get(url, headers={'user-key': zomato_key, 'q':query})
    print(json.loads(request.text))
    return None

find_cities(zomato_key, "California")

"""
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
        
        """

def setupZomatoDataBase(data):
    conn = sqlite3.connect('ZomatoData.sqlite')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS ZomatoData(entity_type TEXT UNIQUE, entity_id INTEGER UNIQUE, city_name TEXT, city_id INTEGER UNIQUE)')

    for zomato in data['location_suggestions']:
        _entity_type = zomato['entity_type']
        _entity_id = zomato['entity_id']
        _city_name = zomato['city_name']
        _city_id = zomato['city_id']

        cur.execute('INSERT OR IGNORE INTO ZomatoData(entity_type, entity_id, city_name, city_id) VALUES (?,?,?,?)', (_entity_type, _entity_id, _city_name, _city_id))
        conn.commit()
    
"""
data1 = getLocationDetails(zomato_key, "New York City")
data2 = getLocationDetails(zomato_key, "Los Angeles")
data3 = getLocationDetails(zomato_key, "Detroit")
data4 = getLocationDetails(zomato_key, "Chicago")
data5 = getLocationDetails(zomato_key, "Ann Arbor")


print(data1)
print(data2)
print(data3)
print(data4)
print(data5)

"""
setupZomatoDataBase(data)
setupZomatoDataBase(data2)

"""
