"""Race condition advent of code day 2024"""
import heapq
file = open("maze.txt", "r")
map_data = [list(x) for x in file.read().split("\n")]
print(map_data)
START = tuple()
END = tuple()
for i, row in enumerate(map_data):
    for j, ele in enumerate(row):
        if ele == 'S':
            START = (i, j)
        if ele == 'E':
            END = (i, j)


Q = []
def search_map(maze_map):
    SEEN = []
    DIRS = [(-1, 0), (0, 1), (1,0), (0, -1)]
    dist = 0
    best_dist = None
    heapq.heappush(Q, (START[0], START[1], DIRS[0], 0))
    heapq.heappush(Q, (START[0], START[1], DIRS[1], 0))
    heapq.heappush(Q, (START[0], START[1], DIRS[2], 0))
    heapq.heappush(Q, (START[0], START[1], DIRS[3], 0))
    while len(Q) != 0:
        y_coords, x_coords, direction, dist = heapq.heappop(Q)

        y_coords += direction[0]
        x_coords += direction[1]
        if y_coords < 0 or y_coords >= len(maze_map):
            continue

        if x_coords < 0 or x_coords >= len(maze_map):
            continue

        if maze_map[y_coords][x_coords] == '#':
            continue
        if maze_map[y_coords][x_coords] == '1':
            cheat_activated_coords_y = y_coords
            cheat_activated_coords_x = x_coords

        if maze_map[y_coords][x_coords] == '2':
            cheat_activated_coords_y_two = y_coords
            cheat_activated_coords_x_two = x_coords

            

        if maze_map[y_coords][x_coords] == 'E' and best_dist is None:
            SEEN.append((y_coords, x_coords, direction))
            best_dist = dist + 1
            return best_dist, SEEN
        elif maze_map[y_coords][x_coords] == 'E' and dist is not None and dist < best_dist:
            best_dist = dist + 1
        if (y_coords, x_coords, direction) in SEEN:
            continue
        else:
            SEEN.append((y_coords, x_coords, direction))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[0], dist + 1))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[1], dist + 1))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[2], dist + 1))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[3], dist + 1))
    return best_dist, SEEN

list_of_maps = []
removed_walls_set = set()

for i, row in enumerate(map_data[:-1]):
    for j, ele in enumerate(row[:-1]):
        if ele == '#':
            if map_data[i][j+1] == '#':
                removed_walls_set.add( ((i,j), (i, j+1)))
            if map_data[i+1][j] == '#':
                removed_walls_set.add(((i,j), (i+1, j)))
            removed_walls_set.add((i,j))

base_best_dist, PATH = search_map(map_data)

NEW_PATH = []
for step in PATH:
    NEW_PATH.append((step[0], step[1]))

speedup_list = []
for step in NEW_PATH:
    if (step[0] + 2, step[1]) in NEW_PATH:
        START = (step[0] + 2, step[1])
        new_temp, _ = search_map(map_data)

    if (step[0] + 2, step[1]) in NEW_PATH:
        START = (step[0] + 2, step[1])
        new_temp, _ = search_map(map_data)



    


    
                
            

