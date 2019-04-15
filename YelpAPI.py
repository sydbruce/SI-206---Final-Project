import requests
import json
import Keys

Yelp_ClientID = Keys.client_ID
YelpAPIKey = Keys.API_Key
headers = {'Authorization': 'Bearer %s' % YelpAPIKey}
url = 'https://api.yelp.com/v3/businesses/search'

params = {'term': 'food', 'location': 'Ann Arbors'}
req = requests.get(url,params=params, headers=headers)
print('The status code is {}'.format(req.status_code))
print(json.loads(req.text))

