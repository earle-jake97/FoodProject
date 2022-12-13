from unicodedata import category
from urllib.request import urlopen
from serpapi import GoogleSearch
import requests, json, random

api_key = 'bMoLYFSZBuVIUdlxfE3w2Hcr2qdhlWQ6'
pos_key = '184b25285db8befa4cc26444b0bd460e'
serp_key = 'edff631da8712e0b4e02e9cc296a4d9cc1f4e5af6bca5270ade21c335a3c438b'

#address = input("\nWhat is your address? (address, city)\n")
#serpAPI params
params = {
  "q": "",
  "tbm": "isch",
  "ijn": "0",
  "api_key": serp_key
}


def get_food_list(address, radius):
    address = address.replace(" ", "%20")
    coordUrl = "http://api.positionstack.com/v1/forward?access_key="+pos_key+"&query="+address
    coords = urlopen(coordUrl)
    y = json.loads(coords.read())
    lat = str(y["data"][0]["latitude"])
    lon = str(y["data"][0]["longitude"])
    #radius = input("\nWhat mile radius? (5-20)\n")
    #converts miles to meters
    radius = float(radius)*1609.34
    radius = str(radius)
    #category for restaurants under tomtom's api
    category1 = "7315"
    urlFastFood = "https://api.tomtom.com/search/2/categorySearch/restaurant.json?key="+api_key+"&lat="+lat+"&lon="+lon+"&radius="+radius+"&categoryset="+category1+"&limit=50"
    response = urlopen(urlFastFood)
    y = json.loads(response.read())
    x = 0
    foodList = []
    #iterates through json and retrieves names of all restaurants
    for item in y["results"]:
        foodList.append(y["results"][x]['poi']['name'])
        x+=1
    #picks a random restaurant from list of all restaurants nearby
    return foodList

def get_food(foodList):
    #picks a random restaurant from list of all restaurants nearby
    if len(foodList) > 0:
        food = random.choice(foodList)
        foodList.remove(food)
        return food
    else:
        return "Out of options!"

def get_image(searchWord):
    params["q"] = searchWord
    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results["images_results"]
    return images_results[0]["thumbnail"]