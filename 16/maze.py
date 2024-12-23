import heapq
import sys
sys.setrecursionlimit(100000)

def read_file():
    maze_file = open("maze.txt")
    maze_map = [list(row) for row in maze_file.read().split("\n")]
    return maze_map

maze = read_file()
elk_coords_y = 0
elk_coords_x = 0
answ_coords_y = 0
answ_coords_x = 0

for index_i, row in enumerate(maze):
    for index_j, ele in enumerate(row):
        if ele == 'E':
            elk_coords_y = index_i
            elk_coords_x = index_j
        if ele == 'S':
            answ_coords_y = index_i
            answ_coords_x = index_j

DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
print(f"Elk coords y is {elk_coords_y} and elk coords x is {elk_coords_x}")
Q = []
d = 0
heapq.heappush(Q, (d, answ_coords_y, answ_coords_x, 1))
#heapq.heappush(Q, (d, elk_coords_y, elk_coords_x, 1))
#heapq.heappush(Q, (d, elk_coords_y, elk_coords_x, 2))
#heapq.heappush(Q, (d, elk_coords_y, elk_coords_x, 3))

SEEN = set()

DIST = {}
best = None
while len(Q) != 0:
    curr_dist,curr_y, curr_x, curr_dir = heapq.heappop(Q)
    #print(f"len of Q is {len(Q)} curr_direction is {curr_dir} curr y is {curr_y} curr x is {curr_x} curr_dist is {curr_dist}")

    if (curr_y, curr_x, curr_dir) not in DIST:
        DIST[(curr_y,curr_x, curr_dir)] = curr_dist
    if (curr_y, curr_x, curr_dir) in SEEN:
        continue
    SEEN.add((curr_y, curr_x, curr_dir))
    if curr_y == elk_coords_y and curr_x == elk_coords_x and best is None:
        #print(f"S found {curr_y} {curr_x}")
        best = curr_dist

    old_x = curr_x
    old_y = curr_y
    curr_y += DIRS[curr_dir][0]
    curr_x += DIRS[curr_dir][1]
    
    if curr_y >= 0 and curr_x >= 0 and curr_y < len(maze) and curr_x < len(maze[0]) and maze[curr_y][curr_x] != '#':
        heapq.heappush(Q, (curr_dist+1, curr_y, curr_x, curr_dir))
    heapq.heappush(Q,(curr_dist+1000, old_y, old_x, (curr_dir + 1) % 4))
    heapq.heappush(Q,(curr_dist+1000, old_y, old_x, (curr_dir + 3) % 4))

print(best)









    

