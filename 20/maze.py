"""Race condition advent of code day 2024"""
import heapq
file = open("maze.txt", "r")
map_data = [x for x in file.read().split("\n")]
START = tuple()
END = tuple()
for i, row in enumerate(map_data):
    for j, ele in enumerate(row):
        if ele == 'S':
            START = (i, j)
        if ele == 'E':
            END = (i, j)


Q = []

SEEN = set()
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
    if y_coords < 0 or y_coords >= len(map_data):
        continue

    if x_coords < 0 or x_coords >= len(map_data):
        continue

    if map_data[y_coords][x_coords] == '#':
        continue

    if map_data[y_coords][x_coords] == 'E' and best_dist is None:
        best_dist = dist
    elif map_data[y_coords][x_coords] == 'E' and dist is not None and dist < best_dist:
        best_dist = dist
    if (y_coords, x_coords, direction) in SEEN:
        continue
    else:
        SEEN.add((y_coords, x_coords, direction))
    heapq.heappush(Q, (y_coords, x_coords, DIRS[0], dist + 1))
    heapq.heappush(Q, (y_coords, x_coords, DIRS[1], dist + 1))
    heapq.heappush(Q, (y_coords, x_coords, DIRS[2], dist + 1))
    heapq.heappush(Q, (y_coords, x_coords, DIRS[3], dist + 1))

print(best_dist)



