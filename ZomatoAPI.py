
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
    print(json.loads(req.text))
    return None
    
def getEstablishments(zomato_key, city_id):
        city = getZomato(zomato_key, "New York City")
        for item in 

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

data = getZomato(zomato_key, "New York City")  
data2 = getZomato(zomato_key, "Detroit")
data3 = getZomato(zomato_key, "Los Angeles") 
data4 = getZomato(zomato_key, "Ann Arbor") 
data5 = getZomato(zomato_key, "Chicago")      

"""
setupZomatoDataBase(data)
setupZomatoDataBase(data2)

"""
