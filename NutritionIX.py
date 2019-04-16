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

def get_nutrition_info(food_item):
    return nix.search(food_item).json()

def save_info(data):
    
