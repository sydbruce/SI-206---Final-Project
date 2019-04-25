
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
        
        

def setupZomatoDataBase(data):
    conn = sqlite3.connect('ZomatoData.sqlite')
    cur = conn.cursor()
    _city_restaurants_price_range_total = 0
    _city_restaurants_price_range_average = 0
    _city_restaurants_aggregate_rating_total = 0
    _city_restaurants_aggregate_rating_average = 0

    cur.execute('CREATE TABLE IF NOT EXISTS ZomatoData(city_name TEXT, popularity TEXT, nightlife_index TEXT, best_rated_restaurant_name TEXT, best_rated_restaurant_price_range INTEGER, best_rated_restaurant_aggregate_rating TEXT, city_restaurants_price_range_average INTEGER, city_restaurants_aggregate_rating_average INTEGER)')
    
    for i in range(10):
            _city_name = data['location']['city_name']
            _popularity = data['popularity']
            _nightlife_index = data['nightlife_index']
            _best_rated_restaurant_name = data['best_rated_restaurant'][i]['restaurant']['name']
            _best_rated_restaurant_price_range = data['best_rated_restaurant'][i]['restaurant']['price_range']
            _best_rated_restaurant_aggregate_rating = data['best_rated_restaurant'][i]['restaurant']['user_rating']['aggregate_rating']
            
            #The calculations are below, final average number shown in 10th best restaurant for each city
            _city_restaurants_price_range_total += data['best_rated_restaurant'][i]['restaurant']['price_range']
            _city_restaurants_price_range_average = _city_restaurants_price_range_total / (i+1)
            _city_restaurants_aggregate_rating_total += float(data['best_rated_restaurant'][i]['restaurant']['user_rating']['aggregate_rating'])
            _city_restaurants_aggregate_rating_average =_city_restaurants_aggregate_rating_total / (i+1)
            
            cur.execute('INSERT INTO ZomatoData(city_name, popularity, nightlife_index, best_rated_restaurant_name, best_rated_restaurant_price_range, best_rated_restaurant_aggregate_rating, city_restaurants_price_range_average, city_restaurants_aggregate_rating_average) VALUES (?,?,?,?,?,?,?,?)', (_city_name, _popularity, _nightlife_index, _best_rated_restaurant_name, _best_rated_restaurant_price_range, _best_rated_restaurant_aggregate_rating, _city_restaurants_price_range_average, _city_restaurants_aggregate_rating_average))
            conn.commit()

#For visualizations: I can look at city popularity, nightlife_index, best_restaurant price/rating, city_restaurants average price/rating
   
data1 = setupZomatoDataBase(getLocationDetails(zomato_key, "Atlanta"))
data2 = setupZomatoDataBase(getLocationDetails(zomato_key, "Boston"))
data3 = setupZomatoDataBase(getLocationDetails(zomato_key, "Chicago"))
data4 = setupZomatoDataBase(getLocationDetails(zomato_key, "Detroit"))
data5 = setupZomatoDataBase(getLocationDetails(zomato_key, "Houston"))
data6 = setupZomatoDataBase(getLocationDetails(zomato_key, "Los Angeles"))
data7 = setupZomatoDataBase(getLocationDetails(zomato_key, "New York City"))
data8 = setupZomatoDataBase(getLocationDetails(zomato_key, "Philadelphia"))
data9 = setupZomatoDataBase(getLocationDetails(zomato_key, "San Francisco"))
data10 = setupZomatoDataBase(getLocationDetails(zomato_key, "Seattle"))


