import heapq

file = open("memory.txt", "r")
data = [x for x in  file.read().split("\n")]
SIZE = 71
DATA_MAP = [['.']* SIZE for i in range(SIZE)]
GOAL_Y = SIZE - 1 
GOAL_X = SIZE - 1

counter = 0
for line in data:
    if counter >= 1024:
        break
    counter += 1
    nums = line.split(",")
    DATA_MAP[int(nums[1])][int(nums[0])] = '#'
    
for line in DATA_MAP:
    print(line)


Q = []
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
SEEN = set()
d = 0
heapq.heappush(Q, (0,0, 0, d))
heapq.heappush(Q, (0,0, 1, d))
heapq.heappush(Q, (0,0, 2, d))
heapq.heappush(Q, (0,0, 3, d))
DATA_MAP[0][0] = 'O'

def search(map):
    best = None
    counter = 0
    while len(Q) != 0:
        counter += 1
        #for row in map:
            #print(row)
        curr_y, curr_x, curr_dir, curr_dist = heapq.heappop(Q)
        curr_y = curr_y + DIRS[curr_dir][0]
        curr_x = curr_x + DIRS[curr_dir][1]
        #print(f"Curr y is {curr_y} curr x is {curr_x}")
        if curr_y < 0 or curr_y >= SIZE:
            continue
        if curr_x < 0  or curr_x >= SIZE:
            continue
        if map[curr_y][curr_x] == '#':
            continue

        if curr_y == GOAL_Y and curr_x == GOAL_X:
            if best is None:
                best = curr_dist
            elif best is not None and best > curr_dist:
                best = curr_dist
            continue

        if (curr_y, curr_x, curr_dir) in SEEN:
            continue
        else:
            SEEN.add((curr_y, curr_x, curr_dir))
            map[curr_y][curr_x] = curr_dir
        heapq.heappush(Q, (curr_y, curr_x, 0, curr_dist + 1))
        heapq.heappush(Q, (curr_y, curr_x, 1, curr_dist + 1))
        heapq.heappush(Q, (curr_y, curr_x, 2, curr_dist + 1))
        heapq.heappush(Q, (curr_y, curr_x, 3, curr_dist + 1))
    return best
best = search(DATA_MAP)
for row in DATA_MAP:
    print(row)
#print(DATA_MAP)
print(best)

