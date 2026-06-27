import numpy as np


def rect(axb:str, screen:np.ndarray)-> np.ndarray:
    a,b = map(int, axb.split("x"))
    screen[0:b, 0:a] = 1
    return screen

def rot_row(ya:str, b:str, screen:np.ndarray)-> np.ndarray:
    row_indx = int(ya.split("=")[1])
    b = int(b)
    screen[row_indx] = np.roll(screen[row_indx], b)
    return screen

def rot_col(ya:str, b:str, screen:np.ndarray)-> np.ndarray:
    col_indx = int(ya.split("=")[1])
    b = int(b)
    screen[:,col_indx] = np.roll(screen[:,col_indx], b)
    return screen

def main(line:str, screen:np.ndarray)->np.ndarray:
    commands = line.split()
    if commands[0] == "rect":
        return rect(commands[1], screen)
    elif commands[0] == "rotate" and commands[1] == "row":
        return rot_row(commands[2], commands[-1], screen)
    elif commands[0] == "rotate" and commands[1] == "column":
        return rot_col(commands[2], commands[-1], screen)

if __name__ == '__main__':
    screen = np.zeros([6, 50])

    test_lines = """rect 3x2
    rotate column x=1 by 1
    rotate row y=0 by 4
    rotate column x=1 by 1"""

    with open("inputs/Day8.txt") as file:
        in_lines = file.read()

    lines = list(map(str.strip, in_lines.strip().splitlines()))

    for line in lines:
        screen = main(line, screen)

    print(screen.sum())