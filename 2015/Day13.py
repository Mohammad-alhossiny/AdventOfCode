import pandas as pd
import itertools
import math


with open("2015\Inputs\Day13.txt", "r") as file:
    content = file.read()


def extract_list(content:str) -> pd.DataFrame:
    seating = pd.DataFrame(columns=["Setter", "Neighbour", "Happiness"])
    for line in content.split("\n"):
        line = line.split() 
        if line:
            if line[2] == "gain":
                happiness = int(line[3])
            elif line[2] == "lose":
                happiness =  -int(line[3])
            else:
                print("Code broke")
                print(line)
                quit()

            setter = line[0]
            neighbour = line[-1].removesuffix(".")

            seating.loc[len(seating.index)] = [setter, neighbour, happiness]
    return seating

def happiness_score(seating_table:pd.DataFrame, permutation:list) -> int:
    happiness = 0
    for index, person in enumerate(permutation):
        happiness_n1 = seating_table.loc[(seating_table["Setter"] == person)&(seating_table["Neighbour"] == permutation[index-1]), "Happiness"]
        
        if (index + 1) == len(permutation):
            happiness_n2 = seating_table.loc[(seating_table["Setter"] == person)&(seating_table["Neighbour"] == permutation[0]), "Happiness"]
        else:
            happiness_n2 = seating_table.loc[(seating_table["Setter"] == person)&(seating_table["Neighbour"] == permutation[index+1]), "Happiness"]

        if not happiness_n1.empty:
            happiness_n1 = happiness_n1.iloc[0]
        else:
            happiness_n1 = 0        
        
        if not happiness_n2.empty:
            happiness_n2 = happiness_n2.iloc[0]
        else:
            happiness_n2 = 0        
        personal_happiness = happiness_n1 + happiness_n2
        happiness += personal_happiness
    return happiness

if __name__ == "__main__":
    #Running a python script ~40,000 times takes a shitload of time, who could've guessed?
    seating_table = extract_list(content)
    people = seating_table["Setter"].unique()

    for person in people:
        seating_table.loc[len(seating_table.index)] = [" Me", person, 0]
        seating_table.loc[len(seating_table.index)] = [person, " Me", 0]
    people = list(people)
    people.append("Me")


    scores = {}
    permutations = list(itertools.permutations(people))
    for permutation in permutations[:(math.factorial(len(people)))+1]:
        permus_happiness_score = happiness_score(seating_table, permutation)
        scores[permutation] = permus_happiness_score

        print(permutation, "\n", permus_happiness_score)


    max_key = max(scores, key=scores.get)
    max_value = scores[max_key]

    print("Key for the largest value:", max_key)  
    print("Largest value:", max_value)  
