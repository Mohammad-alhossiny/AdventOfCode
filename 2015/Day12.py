import json

with open("2015\Inputs\Day12.txt", "r") as in_file:
    in_obs = json.loads(in_file.read())

def return_items(in_obj):
    items = []
    if isinstance(in_obj, dict):
        if "red" in in_obj.values(): #These 2 lines modify for part 2, for part 1 remove this if statement 
             pass
        else:
            for item in in_obj.values():
                    a = return_items(item)
                    items.extend(a)

    elif isinstance(in_obj, list):
        for item in in_obj:
                a = return_items(item)
                items.extend(a)
    else:
        items.append(in_obj)
    
    return items

            
list_oitems = return_items(in_obs)
summ = 0
for i in list_oitems:
    try: 
        summ += i
    except:
        pass

print(summ)