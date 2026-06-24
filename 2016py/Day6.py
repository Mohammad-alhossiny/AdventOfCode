# counts = {}
#   counts[letter] = counts.get(letter, 0) + 1

def main(lines:list[[str]])->str:
    length = len(lines[0])
    message = ""
    for i in range(length):
        counts = {}
        for line in lines:
            counts[line[i]] =counts.get(line[i], 0) + 1
        message += (max(counts, key=counts.get))
    return message

def main2(lines:list[[str]])->str:
    length = len(lines[0])
    message = ""
    for i in range(length):
        counts = {}
        for line in lines:
            counts[line[i]] =counts.get(line[i], 0) + 1
        message += (min(counts, key=counts.get))
    return message

if __name__ == '__main__':
    test = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

    with open("inputs/Day6.txt") as file:
        in_lines = file.read()
    lines = list(map(str.strip, in_lines.strip().splitlines()))

    print(main2(lines))