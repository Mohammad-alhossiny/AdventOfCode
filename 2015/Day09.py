in_str = """Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127
"""
# Travelling salesman, brute forcing it
import pandas as pd
from itertools import permutations

def extract_edge(line:str):
    l = line.split()
    start = l[0]
    end = l[2]
    dist = l[-1]

    return start, end, dist

def calc_dist(route:iter, dist_df):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += int(dist_df.loc[route[i], route[i+1]])
    return total_dist

def brute_force(cities, df):
    shortest_dist = float("inf") 
    for perm in permutations(cities):
        dist =calc_dist(perm, df)
        
        if dist < shortest_dist:
            shortest_dist = dist
            shortest_path = list[perm]
    return shortest_dist, shortest_path

def brute_force_long(cities, df):
    longest_dist = 0
    for perm in permutations(cities):
        dist = calc_dist(perm, df)
        
        if dist > longest_dist:
            longest_dist = dist
            longest_path = list[perm]
    return longest_dist, longest_path

if __name__ == "__main__":
    cities = []
    for line in in_str.split("\n"):
        if line:
            start, end, dist = extract_edge(line)   
            cities.append(start)
            cities.append(end)
    cities = list(set(cities))
    df = pd.DataFrame(columns=cities, index=cities)

    for line in in_str.split("\n"):
        if line:
            start, end, dist = extract_edge(line)   
            df.loc[start, end] = dist
            df.loc[end, start] = dist
    print(df)    
    print(brute_force_long(cities, df))

