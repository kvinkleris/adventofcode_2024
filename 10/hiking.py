file = open("hiking.txt", "r")
data = list(file.read().split("\n"))
TRAILS = []
for row in data:
    TRAILS.append(list([int(x) for x in row] ))
LEN_TRAIL_Y = len(TRAILS)
LEN_TRAIL_X = len(TRAILS[0])

def execute_DFS(y_coords, x_coords, trail  = None):
    if trail is None:
        trail = set()

    #print(trail)
    #trail.append((y_coords, x_coords))

    if TRAILS[y_coords][x_coords] == 9:
        trail.add((y_coords, x_coords))
        return trail
    if y_coords + 1 >= 0 and y_coords + 1 < LEN_TRAIL_Y and TRAILS[y_coords + 1][x_coords] - TRAILS[y_coords][x_coords] == 1:
        execute_DFS(y_coords + 1, x_coords, trail)
    if (y_coords - 1 >= 0) and (y_coords - 1 < LEN_TRAIL_Y) and (TRAILS[y_coords - 1][x_coords] - TRAILS[y_coords][x_coords] == 1):
        execute_DFS(y_coords - 1, x_coords, trail)
    if x_coords + 1 >= 0 and x_coords + 1 < LEN_TRAIL_X and TRAILS[y_coords ][x_coords + 1] - TRAILS[y_coords][x_coords ] == 1:
        execute_DFS(y_coords , x_coords + 1, trail)
    if x_coords - 1 >= 0 and x_coords - 1 < LEN_TRAIL_X and TRAILS[y_coords ][x_coords - 1] - TRAILS[y_coords][x_coords] == 1:
        execute_DFS(y_coords, x_coords - 1, trail)
    return trail

def execute_second_part(y_coords, x_coords, trail  = None):
    if trail is None:
        trail = []

    #print(trail)
    trail.append((TRAILS[y_coords][x_coords]))

    if TRAILS[y_coords][x_coords] == 9:
        return trail
    if y_coords + 1 >= 0 and y_coords + 1 < LEN_TRAIL_Y and TRAILS[y_coords + 1][x_coords] - TRAILS[y_coords][x_coords] == 1:
        execute_second_part(y_coords + 1, x_coords, trail)
    if (y_coords - 1 >= 0) and (y_coords - 1 < LEN_TRAIL_Y) and (TRAILS[y_coords - 1][x_coords] - TRAILS[y_coords][x_coords] == 1):
        execute_second_part(y_coords - 1, x_coords, trail)
    if x_coords + 1 >= 0 and x_coords + 1 < LEN_TRAIL_X and TRAILS[y_coords ][x_coords + 1] - TRAILS[y_coords][x_coords ] == 1:
        execute_second_part(y_coords , x_coords + 1, trail)
    if x_coords - 1 >= 0 and x_coords - 1 < LEN_TRAIL_X and TRAILS[y_coords ][x_coords - 1] - TRAILS[y_coords][x_coords] == 1:
        execute_second_part(y_coords, x_coords - 1, trail)
    return trail

answer_list = []
for i_index, row in enumerate(TRAILS):
    for index_j, _ in enumerate(row):
        if TRAILS[i_index][index_j] == 0:
            answer_list.append(execute_second_part(i_index, index_j))
answ_count = 0

print(answer_list)
for item in answer_list:
    for number in item:
        if number == 9:
            answ_count += 1
print(answ_count)