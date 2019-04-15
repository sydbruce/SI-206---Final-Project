import requests
import json
import Keys
import sqlite3

#Nutritionix Key Configuration

appID = Keys.appID
appKey = Keys.appKey

from nutritionix import Nutritionix
nix = Nutritionix(app_id = appID, api_key = appKey)

def get_nutrition_info(food_item):
    return nix.search(food_item).json()

print(get_nutrition_info("Big Mac"))
print(get_nutrition_info("Pizza"))

#def setupDatabase()
