from sqlalchemy import false


def parser(file_name:str)-> list[list[int]]:
    reports = []
    with open(file_name, "r") as file:
        for line in file.read().strip().split("\n"):
            reports.append(line.split())
        reports = [list(map(int, report)) for report in reports]
    return reports

reports = parser("inputs/Day2.txt")

def safety(report):
    ascent = True
    descent = True
    for i in range(len(report)-1):
        if report[i] > report[i+1]:
            descent = False
        elif report[i] < report[i+1]:
            ascent = False

        if abs(report[i] - report[i+1]) > 3 or report[i] == report[i+1]:
            return False

    if ascent or descent:
        return True
    else:
        return False

safes = 0
for reprt in reports:
    if safety(reprt):
        safes += 1

print(safes)


# by u/Independent_Check_62

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

data = reports

safe_count = sum([is_safe(row) for row in data])
print(safe_count)

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
print(safe_count)
