from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import apiscript
from fastapi.middleware.cors import CORSMiddleware
import pdb


app = FastAPI()
origins = [
    "http://localhost:3000",
]
foodList = []
foodResult = ''

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class UserInfo(BaseModel):
    address: str
    radius: int
    city: str

@app.get("/")
def read_root():
    return {"Home": "Root"}
    
@app.post("/find-restaurants")
def find_restaurants(userInfo: UserInfo):
    global foodList
    foodList = apiscript.get_food_list(userInfo.address, userInfo.radius)
    return foodList

@app.post("/pick-restaurant")
def pick_restaurant(userInfo: UserInfo):
    response = {}
    response["food"] = apiscript.get_food(foodList)
    response["image"] = apiscript.get_image(response["food"] + " " + userInfo.city)
    return response