from itertools import combinations_with_replacement
from collections import Counter

def get_dict(in_str:str) -> dict:
    ingredients = {}
    for line in in_str.split("\n"):
        if line:
            line_list = line.split()
            ingredient = line_list[0][:-1]
            prop_dict = {key:int(value.strip(",")) for key,value in zip(line_list[1::2], line_list[2::2])}
            ingredients[ingredient] = prop_dict
    
    return ingredients

#brute force seems like a really bad idea, but i'm tempted
# fuck it, we ball

def calc_score(ingredients:dict, ingredient_amount:dict) -> int:
    # ingredients = {"name": {capacity:n, durability:n, flavor:n, texture:n}, ...}
    #amount = {"name": n, ...}
    capacity = sum([value["capacity"]*ingredient_amount[key] for key,value in ingredients.items()])
    durability = sum([value["durability"]*ingredient_amount[key] for key,value in ingredients.items()])
    flavor = sum([value["flavor"]*ingredient_amount[key] for key,value in ingredients.items()])
    texture = sum([value["texture"]*ingredient_amount[key] for key,value in ingredients.items()])
    calories = sum([value["calories"]*ingredient_amount[key] for key,value in ingredients.items()])

    if any(x <= 0 for x in [capacity, durability, flavor, texture]):
        score = 0
    elif calories != 500:  # remove this elif for part1
        score = 0 
    else:
        score = capacity*durability*flavor*texture
    
    return score

def get_optimal_cookie(ingredients: dict):
    combos = list(combinations_with_replacement(ingredients.keys(), 100))
    scores = []
    for combo in combos:
        ingredient_amount = Counter(combo)
        scores.append(calc_score(dict(ingredients), ingredient_amount))
    return  max(scores)

input_string = """Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
""" 

if __name__ == "__main__":
    ingredients = get_dict(input_string)
    print(get_optimal_cookie(ingredients))