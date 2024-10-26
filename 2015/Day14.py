def dist_travelled(speed:int, dauration:int, rest:int, time:int) -> int:
    complete_movement_time = dauration + rest
    n_complete_movements = time // complete_movement_time
    partial_movement_time = time % complete_movement_time

    dist_complete = n_complete_movements * speed * dauration
    dist_partial = speed * min(partial_movement_time, dauration) 
    dist = dist_complete + dist_partial

    return dist


def extract_list(string: str) -> list:
    str_lst = string.split()
    deer_name = str_lst[0]
    speed = int(str_lst[3])
    dauration = int(str_lst[6])
    pause = int(str_lst[-2])

    return [deer_name, speed, dauration, pause]

if __name__ == "__main__":
    r_deer = {}
    scores = {}
    with open("2015\Inputs\Day14.txt", "r") as file:
        lines = file.read()

    lines = lines.split("\n")
    for line in lines:
        if line:
            deer_name, speed, dauration, pause = extract_list(line)
            r_deer[deer_name] = [speed, dauration, pause]
            scores[deer_name] = 0

    for sec in range(1, 2503): 
        dists = {}
        for deer_name, attributes in r_deer.items():
            d_speed, d_dauration, d_pause = attributes
            dists[deer_name] = dist_travelled(d_speed, d_dauration, d_pause, sec)

        max_dist = max(dists.values())
        for deer, dist in dists.items():
            if dist == max_dist:
                scores[deer] += 1
        
    
    print(sorted(list(scores.items()), key= lambda deer: deer[1]))

        
