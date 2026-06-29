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

# part2, AI assisted because I'm lazy:
def decompressed_length(s, start, end):
    cursor = start
    total = 0

    while cursor < end:
        if s[cursor] != "(":
            total += 1
            cursor += 1
        else:
            right = s.find(")", cursor)
            c, r = map(int, s[cursor + 1:right].split("x"))

            # Recursively compute the length of the next c characters
            total += r * decompressed_length(
                s,
                right + 1,
                right + 1 + c
            )

            # Skip over those c characters
            cursor = right + 1 + c

    return total

def main2(in_string):
    return decompressed_length(in_string, 0, len(in_string))

if __name__ == '__main__':
    test_lines = ["ADVENT", "A(1x5)BC", "(3x3)XYZ", "A(2x2)BCD(2x2)EFG", "(6x1)(1x3)A", "X(8x2)(3x3)ABCY"]

    with open("inputs/Day9.txt") as file:
        in_lines = file.read()

    line = list(map(str.strip, in_lines.strip().splitlines()))[0]
    print(main2(line))