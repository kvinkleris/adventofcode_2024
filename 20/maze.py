"""Race condition advent of code day 2024"""
import heapq
from collections import Counter
file = open("maze.txt", "r")
map_data = [list(x) for x in file.read().split("\n")]
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
    DIST = {}
    DIRS = [(-1, 0), (0, 1), (1,0), (0, -1)]
    dist = 0
    best_dist = None
    heapq.heappush(Q, (START[0], START[1], DIRS[0], 0, [(START[0], START[1])]))
    heapq.heappush(Q, (START[0], START[1], DIRS[1], 0, [(START[0], START[1])]))
    heapq.heappush(Q, (START[0], START[1], DIRS[2], 0, [(START[0], START[1])]))
    heapq.heappush(Q, (START[0], START[1], DIRS[3], 0, [(START[0], START[1])]))
    while len(Q) != 0:
        y_coords, x_coords, direction, dist, PATH = heapq.heappop(Q)

        y_coords += direction[0]
        x_coords += direction[1]
        if y_coords < 0 or y_coords >= len(maze_map):
            continue

        if x_coords < 0 or x_coords >= len(maze_map):
            continue

        if maze_map[y_coords][x_coords] == '#':
            continue

        if (y_coords, x_coords, direction) not in DIST:
            DIST[(y_coords, x_coords, direction)] = dist

        if maze_map[y_coords][x_coords] == 'E' and best_dist is None:
            SEEN.append((y_coords, x_coords, direction))
            PATH = PATH + [(y_coords, x_coords)]
            best_dist = dist + 1
            return best_dist, PATH
        elif maze_map[y_coords][x_coords] == 'E' and dist is not None and dist < best_dist:
            best_dist = dist + 1
        if (y_coords, x_coords, direction) in SEEN:
            continue
        else:
            SEEN.append((y_coords, x_coords, direction))     
        heapq.heappush(Q, (y_coords, x_coords, DIRS[0], dist + 1, PATH + [(y_coords, x_coords)]))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[1], dist + 1, PATH + [(y_coords, x_coords)]))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[2], dist + 1, PATH + [(y_coords, x_coords)]))
        heapq.heappush(Q, (y_coords, x_coords, DIRS[3], dist + 1, PATH + [(y_coords, x_coords)]))
    return best_dist

base_best_dist, BEST_PATH = search_map(map_data)

for item in BEST_PATH:
    map_data[item[0]][item[1]] = 'F'



def print_maze_map_file(maze_map):
    write_file = open("results.txt", "w")
    for row in maze_map:
        write_file.write(str(row))
        write_file.write("\n")
    write_file.close()

print_maze_map_file(map_data)

def cheats(track, max_dist):
    """Calculate possible speedups using cheats"""
    global START
    speedup_counter = Counter()
    for t1, tuple_value in enumerate(track):
        y1 = tuple_value[0]
        x1 = tuple_value[1]
        for t2 in range(t1 + 3, len(track)):
            y2, x2 = track[t2]
            dist = abs(x2 - x1) + abs(y2 - y1)
            if dist <= max_dist and t2 - t1 > dist:
                speedup_counter[t2 - t1 - dist] += 1
    return speedup_counter
speed_counter = cheats(BEST_PATH, 20)
final_answ = 0
print(speed_counter)
for key in speed_counter:
    if key >= 100:
        final_answ += speed_counter[key]
        
print(final_answ)