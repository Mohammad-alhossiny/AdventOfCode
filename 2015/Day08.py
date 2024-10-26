with open("2015\Inputs\Day08.txt", "r") as file:
    full_input = file.read().strip()
# copied from reddit, still dosen't work
print(sum(len(s[:-1]) - len(eval(s)) for s in full_input))
print(sum(2+s.count('\\')+s.count('"') for s in full_input))