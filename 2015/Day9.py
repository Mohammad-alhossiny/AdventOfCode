#Trying Dijkstra
#Thinking I'm so fucking smart, well Dunning my Kruger and call me an idiot because Dijkstra doesn't work for this kind of issue
import math
import pandas as pd


def parse(in_str:str):
    in_df = pd.DataFrame(columns=["Start", "End", "Distance"])
    in_list = in_str.split("\n")

    for line in in_list:
        if line:
            line_df = get_params(line)
            in_df = pd.concat([in_df, line_df], ignore_index=True)
    return in_df

def get_params(line:str):
    line_as_list = line.split()
    start_loc = line_as_list[0]
    end_loc = line_as_list[2]
    distance = int(line_as_list[-1])
    line_dict = {"Start":[start_loc], "End":[end_loc], "Distance":[distance]}
    line_df = pd.DataFrame(line_dict)
    return line_df

def dijkstra(in_df:pd.DataFrame, start_point:str):
    # Make sure the graph is bidirectional
    reverse_df = in_df.copy()
    reverse_df.columns = ["End", "Start", "Distance"]
    in_df = pd.concat([in_df, reverse_df]).drop_duplicates().reset_index(drop=True)

    # initializing a distance table and node lists
    unvisited = pd.unique(in_df[["Start", "End"]].values.ravel())
    distances = pd.DataFrame({"End": unvisited, "Distance": [math.inf] * len(unvisited)})
    distances.loc[distances["End"] == start_point, "Distance"] = 0
    visited = []


    while len(unvisited) > 0:
        current_node = distances.loc[distances["End"].isin(unvisited)].sort_values("Distance").iloc[0]["End"]
        current_distance = distances.loc[distances["End"] == current_node, "Distance"].iloc[0]
        # Update distances to neighboring nodes
        neighbors = in_df[in_df["Start"] == current_node]
        for _, row in neighbors.iterrows():
            neighbor = row["End"]
            if neighbor in unvisited:
                new_distance = distances.loc[distances["End"] == current_node, "Distance"].iloc[0] + row["Distance"]
                if new_distance < distances.loc[distances["End"] == neighbor, "Distance"].iloc[0]:
                    distances.loc[distances["End"] == neighbor, "Distance"] = new_distance

        # Mark the current node as visited
        visited.append(current_node)
        unvisited = unvisited[unvisited != current_node]
    return distances.sort_values("Distance").iloc[-1]


def get_shortest_dist(distance_from_node):
    dist_keys = list(distance_from_node.keys())
    dist_vals = list(distance_from_node.values())
    shortest_distance = min(dist_vals)
    shortest_path_node = dist_keys[dist_vals.index(min(dist_vals))]
    return shortest_path_node, shortest_distance


input_string = """Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127
"""
if __name__ == "__main__":
    df = parse(input_string)
    # result = dijkstra(df, "Tristram")
    # print(result)
    locations = pd.unique(df[["Start", "End"]].values.ravel())
    distances = pd.DataFrame(columns=["Start", "End", "Total distance"])
    for i, location in enumerate(locations):
        if location:
            end_node, dist = dijkstra(df, location)
            distances.loc[i] = [location, end_node, dist]
    print(distances.sort_values("Total distance"))