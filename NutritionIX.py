import requests
import json
import Keys

#Nutritionix Key Configuration
NutritionixAPI = Keys.NutritionixAPI
NutriotinixAuth = Keys.NutriotinixAuth

auth = Keys.OAuthHandler(NutritionixAPI)
auth.set_access_token(NutritionixAPI)