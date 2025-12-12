# did part1 and deleted it, cba part 2
dial = 50
counter = 0

with open("input/Day01.txt") as f:
    moves = f.read().strip().split("\n")

dial_unwrapped = dial

for move in moves:
    direction = move[0]
    amount = int(move[1:])

    movement = amount if direction == "R" else -amount

    old = dial_unwrapped
    new = old + movement

    counter += abs(new // 100 - old // 100)

    dial_unwrapped = new

print(counter)
