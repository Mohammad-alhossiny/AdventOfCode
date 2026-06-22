keypad = [[1, 2, 3],
          [4, 5,6],
          [7,8,9]]
x = y = 1

def move_cursor(x, y, movement):
    if movement == "U" and y>0:
        y -= 1
    elif movement == "D" and y<2:
        y += 1
    elif movement == "L" and x>0:
        x -= 1
    elif movement == "R" and x<2:
        x += 1
    return x,y

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
    print(main(x, y,get_lines(in_str)))