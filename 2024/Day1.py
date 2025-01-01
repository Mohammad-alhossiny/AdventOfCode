def parser(file_name:str)-> list[list[int]]:
    list1 = []
    list2 = []
    with open(file_name, "r") as file:
        for line in file.read().strip().split("\n"):
            i, j = line.split()
            list1.append(int(i))
            list2.append(int(j))
    return [list1, list2]

list1, list2 = parser("inputs/Day1.txt")
print(list1[0], list2[0])
list1.sort()
list2.sort()
print(list1[0], list2[0])


def part1():
    diffsum = 0

    for i, j in zip(list1, list2):
        diffsum += abs(i - j)
    print(diffsum)

def part2():
    simsum = 0
    for i in list1:
        for j in list2:
            if i == j:
                simsum += i
    print(simsum)
