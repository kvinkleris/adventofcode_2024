import heapq

file = open("memory.txt", "r")
data = [x for x in  file.read().split("\n")]
SIZE = 7
DATA_MAP = [['.']*7 for i in range(7)]


counter = 0
for line in data:
    if counter >= 12:
        break
    counter += 1
    nums = line.split(",")
    DATA_MAP[int(nums[1])][int(nums[0])] = '#'
    
for line in DATA_MAP:
    print(line)



DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
SEEN = set()
def search(map, len, y_coords, x_coords, curr_dir):

    if (y_coords, x_coords) in SEEN:


