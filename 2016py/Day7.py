def is_abba(four_letter_str:str)->bool:
    if four_letter_str[:2] == four_letter_str[3:1:-1] and not (four_letter_str[0] == four_letter_str[1] == four_letter_str[2] == four_letter_str[3]):
        return True
    return False

def split_str(in_str:str)->(list[str], list[str]):
    hyper = []
    normal = []
    for i in in_str.split("["):
        if "]" in i:
            h,n = i.split("]")
            hyper.append(h)
            normal.append(n)
        else:
            normal.append(i)
    return normal, hyper

def parse_str(in_str:str)->bool:
    i = 0
    while i+4 <= len(in_str):
        if is_abba(in_str[i:i+4]):
            return True
        else:
            i+=1
    return False

def main(lines:list[str])->int:
    supports_tls = 0
    for line in lines:
        line_supports_tls = False
        normal, hyper = split_str(line)
        for sub_str in normal:
            if parse_str(sub_str):
                line_supports_tls = True
        for sub_str in hyper:
            if parse_str(sub_str):
                line_supports_tls = False
        if line_supports_tls:
            supports_tls += 1
    return supports_tls

if __name__ == '__main__':
    test_str = """abba[mnop]qrst
    abcd[bddb]xyyx
    aaaa[qwer]tyui
    ioxxoj[asdfgh]zxcvbn"""

    with open("inputs/Day7.txt") as file:
        in_lines = file.read()

    lines = list(map(str.strip, in_lines.strip().splitlines()))

    print(main(lines))
