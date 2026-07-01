class Bot:
    def __init__(self, num):
        self.num: str = num
        self.values: list[int] = []
        self.high_target: tuple[str, str] = None
        self.low_target: tuple[str, str] = None


bots: dict[str, Bot] = {}
outputs: dict[str, str] = {}

def add_val(bot, val):
    if bot in bots:
        bots[bot].values.append(val)
    else:
        bots[bot] = Bot(bot)
        bots[bot].values.append(val)


def parse_line(line: str):
    operations = line.split()

    if "value" in line:
        bot = operations[-1]
        val = int(operations[1])
        add_val(bot, val)

    else:
        bot = operations[1]
        low = (operations[5], operations[6])
        high = (operations[-2], operations[-1])

        if bot not in bots:
            bots[bot] = Bot(bot)

        bots[bot].low_target = low
        bots[bot].high_target = high


def give(bot: Bot):

    if len(bot.values) < 2:
        return

    high = max(bot.values)
    low = min(bot.values)


    if bot.low_target[0] == "bot":
        add_val(bot.low_target[1], low)
    else:
        outputs[bot.low_target[1]] = low

    if bot.high_target[0] == "bot":
        add_val(bot.high_target[1], high)
    else:
        outputs[bot.high_target[1]] = high

    bot.values = []     # FIX 3 (important to prevent re-trigger issues)


if __name__ == '__main__':
    test_lines = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

    with open("inputs/Day10.txt") as file:
        in_lines = file.read()

    lines = list(map(str.strip, in_lines.strip().splitlines()))

    for line in lines:
        parse_line(line)

    while True:
        active = [b for b in bots.values() if len(b.values) == 2]

        if not active:
            break

        for bot in active:
            if 61 in bot.values and 17 in bot.values:
                print("the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips is ", bot.num)

            give(bot)

    print("multiply together the values of outputs 0, 1, and 2 = ", outputs["0"]* outputs["1"] * outputs["2"])