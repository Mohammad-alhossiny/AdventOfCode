def is_triangle(tri_list:list):
    x,y,z = tri_list
    if x+y>z and x+z>y and y+z>x:
        return True
    else:
        return False

def part1_lists(lines):
    lines = list(map(str.strip, in_str.strip().splitlines()))
    lists = []
    for line in lines:
        lists.append([int(x) for x in line.split()])
    return lists

def part2_lists(lines):
    lists = part1_lists(lines)
    part2_list = []
    for i in range(int(len(lists)/3)):
        indx = i*3
        part2_list.append([lists[indx][0], lists[indx+1][0], lists[indx+2][0]])
        part2_list.append([lists[indx][1], lists[indx + 1][1], lists[indx + 2][1]])
        part2_list.append([lists[indx][2], lists[indx + 1][2], lists[indx + 2][2]])
    return part2_list

if __name__ == '__main__':
    with open("inputs/Day3.txt") as file:
        in_str = file.read()

    # lists = part1_lists(in_str)
    # valid_tri = list(filter(is_triangle, lists))
    # print(len(valid_tri))

    lists = part2_lists(in_str)
    valid_tri = list(filter(is_triangle, lists))
    print(len(valid_tri))