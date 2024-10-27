import pandas as pd


def get_surround(df:pd.DataFrame, light_index:list) -> pd.DataFrame:
    slice_df = pd.DataFrame(".", index=range(3), columns=range(3))
    rows, cols = df.shape
    for i in range(3):
        for j in range(3):
            row = (light_index[0] -1 ) + i
            col = (light_index[1] -1) + j 
            if 0 <= row < rows and 0 <= col < cols:
                slice_df.iat[i, j] = df.iat[row, col]
    return slice_df

def calc_light_state(slice_df:pd.DataFrame) -> str:
    current_state = slice_df.iat[1,1]
    slice_df.iat[1,1] = "."
    count_on = (slice_df == "#").sum().sum()

    if current_state == "#" and (count_on == 2 or count_on == 3):
        return "#"  
    elif current_state == "." and count_on == 3:
        return "#"  
    else:
        return "."  


def new_lights(df:pd.DataFrame) -> pd.DataFrame:
    shape = df.shape
    new_df = pd.DataFrame('.', index=range(shape[0]), columns=range(shape[1])) 
    for row in range(shape[0]):
        for col in range(shape[1]):
            index = [row, col]
            if index in [[0,0], [0,shape[1]-1], [shape[0]-1,0], [shape[0]-1,shape[1]-1]]:  # part 2, remove if for part 1
                new_df.iat[row, col] = "#"
            else:    
                surrounding = get_surround(df, index)
                light = calc_light_state(surrounding)
                new_df.iat[row, col] = light
        # print(f"row {row} done.")
    return new_df


if __name__ == "__main__":
    with open("2015/Inputs/Day18.txt") as file:
        file = file.read()
    # The first problem to get me to use debugging tools, I like (and fear) it
    # + I think code would run alot faster if i did df.apply instead of func(df), but I cba

    df = pd.DataFrame([list(line) for line in file.strip().split("\n")])
    n = 100
    for i in range(n):
        df = new_lights(df)
        print(f"Step {i+1} out of {n} compelete")
    print(sum(df.apply(pd.Series.value_counts).loc["#"].dropna()))