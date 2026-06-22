def move_cursor(x, y, movement):
    oldx, oldy = x, y
    if movement == "U":
        y -= 1
    elif movement == "D":
        y += 1
    elif movement == "L":
        x -= 1
    elif movement == "R":
        x += 1
    if (
            y < 0 or y >= len(keypad) or
            x < 0 or x >= len(keypad[y]) or
            keypad[y][x] is None):
        return oldx, oldy

    return x, y

def get_lines(in_str:str):
    return map(str.strip, in_str.strip().splitlines())


def main(x,y, lines):
    code = ""
    for line in lines:
        for i in line:
            x,y = move_cursor(x, y, i)
        code += str(keypad[y][x])
    return code





test_str = """ULL
RRDDD
LURDL
UUUUD
"""
with open("inputs/Day2.txt","r") as f:
    in_str = f.read()

if __name__ == "__main__":
    keypad = [  [None, None, 1, None, None],
                [None, 2 ,   3   ,4,  None],
                [5,    6,    7,   8,     9],
                [None, "A", "B", "C", None],
                [None, None,"D", None, None]]
    x = 0
    y = 2

    print(main(x, y,get_lines(in_str)))