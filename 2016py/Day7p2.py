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

def is_bab(three_letter_str:str)->bool:
    if three_letter_str[0] == three_letter_str[2] != three_letter_str[1]:
        return True
    return False

def parse_str(in_str: str) -> list[str]:
    matches = []
    i = 0
    while i + 3 <= len(in_str):
        if is_bab(in_str[i:i+3]):
            matches.append(in_str[i:i+3])
        i += 1
    return matches

def main(lines:list[str])->int:
    supports_ssl = 0
    for line in lines:
        line_supports_ssl = False
        normal, hyper = split_str(line)
        for sub_str in hyper:
            matches = parse_str(sub_str)

            for s in matches:
                for normal_str in normal:
                    if f"{s[1]}{s[0]}{s[1]}" in normal_str:
                        line_supports_ssl = True
        if line_supports_ssl:
            supports_ssl += 1
    return supports_ssl


if __name__ == '__main__':
    test_str = """aba[bab]xyz
    xyx[xyx]xyx
    aaa[kek]eke
    zazbz[bzb]cdb"""

    with open("inputs/Day7.txt") as file:
        in_lines = file.read()

    lines = list(map(str.strip, in_lines.strip().splitlines()))
    print(main(lines))

