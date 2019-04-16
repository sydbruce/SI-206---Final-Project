
import requests
import json


zomato_key = Keys.ZomatoAPI
url = "https://developers.zomato.com/api/v2.1/categories"

params = {'user-key': zomato_key}
req = requests.get(url,params=params)
print('The status code is {}'.format(req.status_code))
print(json.loads(req.text))
