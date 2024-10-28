import re # copied part1, regex id bs

def read(s):
    return [i.strip() for i in open(s, 'r')]
lines = read('2015/Inputs/Day19.txt')

replacements = []
for line in lines[:-2]:
    replacement = re.findall(r'(\S+) => (\S+)', line)
    replacements.append(replacement[0])
target = lines[-1]

def possibles(inm):
    S = set()
    for base, new in replacements:
        for i in range(len(inm)):
            if inm[i:i+len(base)] == base:
                y = inm[:i] + new + inm[i+len(base):]
                S.add(y)
    return S

# reddit says backwards bfs or greedy shit, I cba