def check_id(id:int):
    id = str(id)
    if len(id)%2 == 0:
        mid_point = int(len(id) / 2)
        if id[0:mid_point] == id[mid_point:]:
            return int(id)
        else:
            return 0
    else:
        return 0

def check_range(in_range:str):
    start, end = in_range.split("-")
    start = int(start)
    end = int(end)

    id_sums = 0

    for i in range(start, end+1):
        id_sums += check_id(i)
    return id_sums


with open("input/Day02.txt") as file:
    range_list = file.read().strip().split(",")
    
sums = 0
for i in range_list:
    print(i, check_range(i))
    sums += check_range(i)

print(f"final sum = {sums}")
