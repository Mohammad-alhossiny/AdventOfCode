def main(in_string:str)->int:
    cursor = 0
    len_in_str = 0
    while cursor < len(in_string):
        if in_string[cursor] == "(":
            #(characters x repetition)chars_to _repeat
            left_bracket = cursor
            right_bracket = in_string.find(")", left_bracket)
            c,r = in_string[left_bracket+1 : right_bracket].split("x")
            c = int(c)
            r = int(r)
            len_in_str += c * r
            cursor = right_bracket + c + 1
        else:
            len_in_str += 1
            cursor += 1
    return len_in_str

if __name__ == '__main__':
    test_lines1 = ["ADVENT", "A(1x5)BC", "(3x3)XYZ", "A(2x2)BCD(2x2)EFG", "(6x1)(1x3)A", "X(8x2)(3x3)ABCY"]

    with open("inputs/Day9.txt") as file:
        in_lines = file.read()

    line = list(map(str.strip, in_lines.strip().splitlines()))[0]
    print(main(line))