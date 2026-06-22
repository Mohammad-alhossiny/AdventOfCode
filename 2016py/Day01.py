facing_dirs = ["north", "east", "south", "west"]

def change_facing(facing, letter):
    indx = facing_dirs.index(facing)
    if letter == "R":
        indx += 1
    elif letter == "L":
        indx -= 1
    if indx>3:
        indx = 0
    facing = facing_dirs[indx]
    return facing


def movement(x, y, facing, n):
    if facing == "north":
        y += n
    elif facing == "south":
        y-= n
    elif facing == "east":
        x += n
    elif facing == "west":
        x -= n

    return x,y


def main(directions):
    # direction is "Rn" or "Ln"
    facing = "north"
    x = 0
    y = 0
    for direction in directions:
        facing = change_facing(facing, direction[0])
        x,y = movement(x, y, facing, int(direction[1:]))
    return x,y, abs(x)+abs(y)


def create_dir_list(dir_str:str):
    dir_str = list(map(str.strip, dir_str.strip().split(",")))
    return dir_str

test_str1 = "R2, L3"
test_str2 = "R2, R2, R2"
test_str3 = "R5, L5, R5, R3"

with open("inputs/Day1.txt","r") as f:
    in_str = f.read()

# part2:
def main2(directions):
    facing = "north"
    x = y = 0
    visited = {(0, 0)}
    for direction in directions:
        facing = change_facing(facing, direction[0])
        distance = int(direction[1:])

        for _ in range(distance):
            x, y = movement(x, y, facing, 1)

            if (x, y) in visited:
                return x, y, abs(x) + abs(y)

            visited.add((x, y))

test_str4 = "R8, R4, R4, R8"

if __name__ == "__main__":
    dirs = create_dir_list(in_str)
    print(main2(dirs))
