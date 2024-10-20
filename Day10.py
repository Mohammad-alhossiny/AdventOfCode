from itertools import groupby

def exract_list(line:str) -> list:
    new_l = [''.join(g) for k, g in groupby(line)]
    return new_l

def pronounce(l:list) -> str:
    out_str = ""
    for i in l:
        repeat = str(len(i))
        number = i[0]
        out_str += repeat + number
    return out_str

if __name__ == "__main__":
    in_str = "3113322113"
    for i in range(50):
        in_str = pronounce(exract_list(in_str))

    print(len(in_str))