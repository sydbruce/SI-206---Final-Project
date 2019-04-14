import requests
import json
import Keys

nutritionixAPI = Keys.nutritionixAPI
nutritionixAuth= Keys.nutritionixAuth

auth = tweepy.OAuthHandler(cosnsumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)