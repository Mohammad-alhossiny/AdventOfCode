from itertools import combinations
with open("2015/Inputs/Day17.txt") as file:
    file = file.read()
    
conts = []
for line in file.strip().split("\n"):
    conts.append(int(line))

combs = [comb for r in range(1, len(conts) + 1) for comb in combinations(conts, r) if sum(comb)==150]
print (([ comb  for comb in combs if len(comb) == 4]))