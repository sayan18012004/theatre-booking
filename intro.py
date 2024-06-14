from fastapi import FastAPI
from enum import Enum

app = FastAPI()

food_items = {
    'indian': ["Samosa", "Dosa", "pav bhaji"],
    'american': ["burger", "hotdog"],
    'italian': ["ravioli", "pizza"]
}

valid_Cuisines = food_items.keys()


class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

@app.get("/get_item/{cuisine}")
async def get_item(cuisine: AvailableCuisines):
    return food_items.get(cuisine)



