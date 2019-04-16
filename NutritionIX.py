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
    nutrition = nix.item(id = get_food_id(food_item)).json()
    return nutrition["nf_saturated_fat"]

hii = get_food_nutrition("Big Mac")
print(hii)

### Code Test Area ###
#go = nix.item(id="513fc9e73fe3ffd40300109f").json()
#print(json.dumps(go, indent= 3))

testers = """
{
   "old_api_id": null,
   "item_id": "513fc9e73fe3ffd40300109f",
   "item_name": "Big Mac",
   "leg_loc_id": 114,
   "brand_id": "513fbc1283aa2dc80c000053",
   "brand_name": "McDonald's",
   "item_description": "Burgers & Sandwiches - Big Mac",
   "updated_at": "2018-08-27T18:55:17.000Z",
   "nf_ingredient_statement": null,
   "nf_water_grams": null,
   "nf_calories": 540,
   "nf_calories_from_fat": 260,
   "nf_total_fat": 28,
   "nf_saturated_fat": 10,
   "nf_trans_fatty_acid": 1,
   "nf_polyunsaturated_fat": null,
   "nf_monounsaturated_fat": null,
   "nf_cholesterol": 80,
   "nf_sodium": 950,
   "nf_total_carbohydrate": 45,
   "nf_dietary_fiber": 3,
   "nf_sugars": 9,
   "nf_protein": 25,
   "nf_vitamin_a_dv": 10,
   "nf_vitamin_c_dv": 2,
   "nf_calcium_dv": 10,
   "nf_iron_dv": 25,
   "nf_refuse_pct": null,
   "nf_servings_per_container": null,
   "nf_serving_size_qty": 1,
   "nf_serving_size_unit": "burger",
   "nf_serving_weight_grams": 212,
   "allergen_contains_milk": null,
   "allergen_contains_eggs": null,
   "allergen_contains_fish": null,
   "allergen_contains_shellfish": null,
   "allergen_contains_tree_nuts": null,
   "allergen_contains_peanuts": null,
   "allergen_contains_wheat": null,
   "allergen_contains_soybeans": null,
   "allergen_contains_gluten": null,
   "usda_fields": null
   """