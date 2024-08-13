from handlers.food_handlers import *


food = Food()

food.calories = 3

def poop(wow: Food):
    poop_weight = wow.calories + 7
    print(poop_weight)
    return poop_weight

poop(food)