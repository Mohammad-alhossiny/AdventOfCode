def get_checksum(line:str)->(int, str, str):
    sections = line.strip().split("-")
    id_checksum = sections.pop()
    idn, checksum = id_checksum.split("[")
    checksum = checksum[0:-1]
    room = str.join("", sections)
    return int(idn), checksum, room

def get_room_id(line:str)->(str, int):
    sections = line.strip().split("-")
    id_checksum = sections.pop()
    idn, _ = id_checksum.split("[")
    room = str.join(" ", sections)
    return room, idn

def val_cheksum(cheksum:str, room:str)-> bool:
    counts = {}
    for letter in room:
        counts[letter] = counts.get(letter, 0) + 1
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    clac_checksum = str.join("",[x[0] for x in sorted_items[:5]])
    return clac_checksum==cheksum

def val_list(lines:list[str])->int:
    total = 0
    for line in lines:
        idn, checksum, room = get_checksum(line)
        if val_cheksum(checksum, room):
            total += idn
    return total

def apply_rot(room:str, idn:int)-> str:
    sections = []
    for section in room.split():
        sections.append(''.join(
        chr((ord(c) - ord('a') + idn) % 26 + ord('a'))
        for c in section ))
    return str.join(" ",sections)


test_lines: str = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""

test_cypher = "qzmt-zixmtkozy-ivhz-343[asd]"

if __name__ == '__main__':
    with open("inputs/Day4.txt") as file:
        in_lines = file.read()

    lines = list(map(str.strip, in_lines.strip().splitlines()))

# part 1:
    total = val_list(lines)
    print(total)

# part 2:
    for line in lines:
        room , idn = get_room_id(line)
        rotated = apply_rot(room, int(idn))
        if "North".lower() in rotated:
            print(rotated, idn)