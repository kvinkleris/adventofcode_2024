FILE = open("map.txt")

info = FILE.read().split("\n")

ARRAYS = []

for string in info:
    ARRAYS.append(list(string))

CURR_DIRECTION = 0
POSSIBLE_DIRECTIONS = ['^', '>', 'v', '<']
CURR_LOCATION_X = 0
CURR_LOCATION_Y = 0

MAX_LEN_X = len(ARRAYS)
MAX_LEN_Y = len(ARRAYS[0])

def find_location():
    global CURR_LOCATION_X
    global CURR_LOCATION_Y
    for index, row in enumerate(ARRAYS):
        for j, ele in enumerate(row):
            if ARRAYS[index][j] == '^':
                print("FOUND!")
                print(j)
                print(index)
                CURR_LOCATION_X = j
                CURR_LOCATION_Y = index

def move():
    global CURR_LOCATION_X
    global CURR_LOCATION_Y
    global CURR_DIRECTION
    new_addr_x = CURR_LOCATION_X
    new_addr_y = CURR_LOCATION_Y
    if POSSIBLE_DIRECTIONS[CURR_DIRECTION] == '^':
        new_addr_y -= 1
    if POSSIBLE_DIRECTIONS[CURR_DIRECTION] == '>':
        new_addr_x += 1
    
    if POSSIBLE_DIRECTIONS[CURR_DIRECTION] == '<':
        new_addr_x -= 1

    if POSSIBLE_DIRECTIONS [CURR_DIRECTION] == 'v':
        new_addr_y += 1
    
    if new_addr_x < 0 or new_addr_x > MAX_LEN_X - 1:
        ARRAYS[CURR_LOCATION_Y][CURR_LOCATION_X] = 'X'
        return False
    
    if new_addr_y < 0 or new_addr_y > MAX_LEN_Y -1:
        ARRAYS[CURR_LOCATION_Y][CURR_LOCATION_X] = 'X'
        return False
    
    if ARRAYS[new_addr_y][new_addr_x] == '#':
        CURR_DIRECTION += 1
        if (CURR_DIRECTION >= 4):
            CURR_DIRECTION = 0
        return True
    else:
        ARRAYS[CURR_LOCATION_Y][CURR_LOCATION_X] = 'X'
        CURR_LOCATION_X = new_addr_x
        CURR_LOCATION_Y = new_addr_y
        return True

        
    


print(CURR_LOCATION_Y)

find_location()

while(move() != False):
    for array in ARRAYS:
        pass

answ = 0
for array in ARRAYS:
    for letter in array:
        if letter == 'X':
            answ += 1

print(answ)

