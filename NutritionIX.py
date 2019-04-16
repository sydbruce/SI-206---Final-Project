import requests
import json
import Keys
import sqlite3

#Nutritionix Key Configuration

appID = Keys.appID
appKey = Keys.appKey

def SQLSetup():
    conn = sqlite3.connect("NutritionixData.sql")
    cur = conn.cursor()
    cur.execute("CREATE TABLE ")


from nutritionix import Nutritionix
nix = Nutritionix(app_id = appID, api_key = appKey)

def input_food(food_item):
    return nix.search(food_item).json()

def get_food_id(food_item):
    raw_info = input_food(food_item)
    ID = (raw_info['hits'][0]["_id"])
    return ID

def get_food_nutrition(food_item):
    nutrition = nix.item(get_food_id(food_item)).json()
    return nutrition

hi = get_food_id("Chicken McNuggets")
print(hi)

go = nix.item(id="513fc9e73fe3ffd40300109f").json()
#print(go)

#def get_nutrition_info(food_item):
 #   search_term = nix.search(food_item).json()
  #  data = json.dumps(search_term), indent = 3))
   # return data
    #raw = get_nutrition_info("Chicken McNuggets")
#print(hi)
#print(raw['hits'][0]["_score"])

go = nix.item(id="513fc9e73fe3ffd40300109f").json()
#print(go)
   

#def save_info(data):

    