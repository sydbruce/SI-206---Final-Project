import requests
import json
import Keys

#Nutritionix Key Configuration
appID = Keys.appID
appKey = Keys.appKey

from nutritionix import Nutritionix
nix = Nutritionix(app_id = appID, api_key = appKey)

def get_nutrition_info(api, cacheDict, fname):
    print(nix.search('Big Mac').json())
