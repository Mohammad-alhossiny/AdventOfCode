import numpy as np
import pandas as pd
def parser(file_path):
    with open(file_path, "r") as file:
        lines = file.read().strip().split("\n")
        data = [list(line) for line in lines]
    return pd.DataFrame(data)



def extract_diagonals(df): #chatGPT coded the function
    diagonals = []
    stacked = df.stack()  # Convert the DataFrame into a Series with MultiIndex

    # Primary diagonals (top-left to bottom-right)
    for offset in range(-df.shape[0] + 1, df.shape[1]):
        # Check where (row index - column index) equals the offset
        diagonal = stacked[(stacked.index.get_level_values(0) - stacked.index.get_level_values(1)) == offset].tolist()
        diagonals.append(diagonal)

    # Secondary diagonals (top-right to bottom-left)
    for offset in range(df.shape[0] + df.shape[1] - 1):
        # Check where (row index + column index) equals the offset
        diagonal = stacked[(stacked.index.get_level_values(0) + stacked.index.get_level_values(1)) == offset].tolist()
        diagonals.append(diagonal)

    return pd.DataFrame(diagonals).fillna("O")


# # each directon checks both XMAS and SMAX so no need to double up
def check_horizantal(table:pd.DataFrame):
    total = 0
    for _, row in table.iterrows():
        for start in range(len(row) - 3):
            sli = "".join(str(x) for x in row[start:start + 4])
            if "XMAS" in sli or "SAMX" in sli:
                total += 1
    return total

def check_vertical(table:pd.DataFrame):
    total = 0
    for col in table.columns:
        for start in range(len(table) - 3):
            sli = "".join(str(table.iloc[start+i][col]) for i in range(4))
            if "XMAS" in sli or "SAMX" in sli:
                total += 1
    return total

data = parser("inputs/Day4.txt")
diags = extract_diagonals(data)

print(check_horizantal(data) + check_vertical(data) + check_horizantal(diags))
