with open("./2015/Inputs/Day16.txt") as file:
    in_str = file.read()

aunts = {}
target ={"children": 3, "cats": 7,"samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2,"perfumes": 1}

if __name__ == "__main__":
    for line in in_str.strip().split("\n"):
       line_list = line.split()
       aunts[" ".join(line_list[0:2])] = {key.strip(":"):int(value.strip(",")) for key, value in zip(line_list[2::2], line_list[3::2])}
    
    for aunt in aunts.items():
        # if all(tup[1] == target[tup[0]] for tup in aunt[1].items()):
            # print(aunt)
        greater = False
        lesser = False
        for tup in aunt[1].items():
            if (tup[0] == "cats" or tup[0] == "trees") and (tup[1] > target[tup[0]]):
                greater = True
            
            if (tup[0] == "pomeranians" or tup[0] == "goldfish") and (tup[1] < target[tup[0]]):
                lesser = True
            
        if all(tup[1] == target[tup[0]] for tup in aunt[1].items() if tup[0] not in ["cats", "trees","goldfish", "pomeranians"] ) and greater and lesser:
            print(aunt)