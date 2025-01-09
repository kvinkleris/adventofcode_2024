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
    SEEN = set()
    DIRS = [(-1, 0), (0, 1), (1,0), (0, -1)]
    dist = 0
    best_dist = None
    heapq.heappush(Q, (START[0], START[1], DIRS[0], 0))
    heapq.heappush(Q, (START[0], START[1], DIRS[1], 0))
    heapq.heappush(Q, (START[0], START[1], DIRS[2], 0))
    heapq.heappush(Q, (START[0], START[1], DIRS[3], 0))
    cheat_activated_coords = set()
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
        if maze_map[y_coords][x_coords] == '1' or maze_map[y_coords][x_coords] == '2':
            cheat_activated_coords.add((x_coords, y_coords))

        if maze_map[y_coords][x_coords] == 'E' and best_dist is None:
            best_dist = dist
        elif maze_map[y_coords][x_coords] == 'E' and dist is not None and dist < best_dist:
            best_dist = dist
        if (y_coords, x_coords, direction) in SEEN:
            continue
        else:
            SEEN.add((y_coords, x_coords, direction))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[0], dist + 1))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[1], dist + 1))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[2], dist + 1))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[3], dist + 1))
    return best_dist, cheat_activated_coords

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

base_best_dist, og = search_map(map_data)
time_saved_list = []
counter = 0
file = open("results.txt", "w")
routes_taken = set()
for item in removed_walls_set:
    new_map = [item[:] for item in map_data]

    item1 = item[0]
    item2 = item[1]
    item3 = None
    item4 = None
    if type(item1) is tuple:
        item1 = item[0][0]
        item2 = item[0][1]
        item3 = item[1][0]
        item4 = item[1][1]
    
    if item3 is None and item4 is None:
        #print(new_map[item1][item2])
        new_map[item1][item2] = '1'
    else:
        new_map[item1][item2] = '1'
        new_map[item3][item4] = '2'
    cheat_coords_set = []
    #file.write("------------------------------------- \n")
    #for row in new_map:
        #file.write(str(row))
        #file.write("\n")
    #file.write(f"Speed up is {base_best_dist - search_map(new_map)} \n")
    #file.write("------------------------------------- \n")
    new_dist, cheat_coords = search_map(new_map)
    if cheat_coords not in cheat_coords_set:
        cheat_coords_set.append(cheat_coords)
        time_saved_list.append(base_best_dist - new_dist)
    print(cheat_coords_set)
print(time_saved_list)
    


    
                
            

