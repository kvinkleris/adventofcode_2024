import sys
sys.setrecursionlimit(100000)

def read_file():
    maze_file = open("maze.txt")
    maze_map = [list(row) for row in maze_file.read().split("\n")]
    return maze_map

maze = read_file()
elk_coords_y = 0
elk_coords_x = 0

for index_i, row in enumerate(maze):
    for index_j, ele in enumerate(row):
        if ele == 'E':
            elk_coords_y = index_i
            elk_coords_x = index_j
            break

print(elk_coords_y)
print(elk_coords_x)
scores = []
counter = 0
SEEN = set()
def DFS(elk_y, elk_x, dir, score, seen : set):
    
    if (elk_y, elk_x) in seen:
        return 0
    if maze[elk_y][elk_x] == '#':
        return 0
    if maze[elk_y][elk_x] == 'S':
        scores.append(score)
        return score
    
    seen.add((elk_y, elk_x))
    
    if dir == '>':
        DFS(elk_y - 1, elk_x, '^', score+1001, seen.copy())
        DFS(elk_y, elk_x + 1, '>', score+1, seen.copy())
        DFS(elk_y + 1, elk_x, 'v', score+1001, seen.copy())
    elif dir == '<':
        DFS(elk_y - 1, elk_x, '^', score + 1001, seen.copy())
        DFS(elk_y, elk_x - 1, '<', score + 1, seen.copy() )
        DFS(elk_y + 1, elk_x, 'v', score + 1001, seen.copy())
    elif dir == '^':
        DFS(elk_y - 1, elk_x, '^', score + 1, seen.copy())
        DFS(elk_y, elk_x + 1, '>', score + 1001, seen.copy())
        DFS(elk_y, elk_x - 1, '<', score + 1001, seen.copy())
    elif dir == 'v':
        DFS(elk_y, elk_x + 1, '>', score + 1001, seen.copy())
        DFS(elk_y, elk_x - 1, '<', score + 1001, seen.copy())
        DFS(elk_y + 1, elk_x, 'v', score + 1, seen.copy())
    return score

DFS(elk_coords_y, elk_coords_x, '<', 0, SEEN)
print(scores)
print(min(scores))

    

