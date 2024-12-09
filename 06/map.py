import copy

FILE = open("map.txt")

info = FILE.read().split("\n")

ARRAYS = []

for string in info:
    ARRAYS.append(list(string))

CURR_DIRECTION = 0
POSSIBLE_DIRECTIONS = ['^', '>', 'v', '<']
CURR_LOCATION_X = 0
CURR_LOCATION_Y = 0
DETECTED_LOOPS = 0
STARTING_LOCATION_Y = 0
STARTING_LOCATION_X = 0

MAX_LEN_X = len(ARRAYS)
MAX_LEN_Y = len(ARRAYS[0])

def find_location():
    global CURR_LOCATION_X
    global CURR_LOCATION_Y
    global STARTING_LOCATION_Y
    global STARTING_LOCATION_X
    for index, row in enumerate(ARRAYS):
        for j, ele in enumerate(row):
            if ARRAYS[index][j] == '^':
                #print("FOUND!")
                #print(j)
                #print(index)
                CURR_LOCATION_X = j
                CURR_LOCATION_Y = index
                STARTING_LOCATION_X = j
                STARTING_LOCATION_Y = index

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
    
def move_check_for_loop(temp_array):
    #for line in temp_array:
        #print(line)
    #print("---------------------------")
    global CURR_LOCATION_X
    global CURR_LOCATION_Y
    global CURR_DIRECTION
    global DETECTED_LOOPS
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
        temp_array[CURR_LOCATION_Y][CURR_LOCATION_X] = POSSIBLE_DIRECTIONS[CURR_DIRECTION]
        #print("ESCAPED")
        return False
    if new_addr_y < 0 or new_addr_y > MAX_LEN_Y -1:
        temp_array[CURR_LOCATION_Y][CURR_LOCATION_X] = POSSIBLE_DIRECTIONS[CURR_DIRECTION]
        #print("ESCAPED")
        return False
    if temp_array[new_addr_y][new_addr_x] == '#':
        CURR_DIRECTION += 1
        if (CURR_DIRECTION >= 4):
            CURR_DIRECTION = 0
        return True
    elif POSSIBLE_DIRECTIONS[CURR_DIRECTION] == temp_array[new_addr_y][new_addr_x]:
        print("LOOP DETECTED!")
        DETECTED_LOOPS += 1
        return False
    else:
        temp_array[CURR_LOCATION_Y][CURR_LOCATION_X] = POSSIBLE_DIRECTIONS[CURR_DIRECTION]
        CURR_LOCATION_X = new_addr_x
        CURR_LOCATION_Y = new_addr_y
        return True

find_location()
#for array in ARRAYS:
    #print(array)

#while(move() != False):
 #   pass

#answ = 0
#for array in ARRAYS:
#    for letter in array:
#        if letter == 'X':
 #           answ += 1
steps_taken = 0
for index_y, row in enumerate(ARRAYS):
    for index_x, letter in enumerate(row):
        #print(f"index y is {index_y} index x is {index_x}")
        if letter != '#' and letter != '^':
            modified_array = copy.deepcopy(ARRAYS)
            modified_array[index_y][index_x] = '#'
            CURR_LOCATION_X = STARTING_LOCATION_X
            CURR_LOCATION_Y = STARTING_LOCATION_Y
            CURR_DIRECTION = 0
            modified_array[CURR_LOCATION_Y][CURR_LOCATION_X] = '.'

            #for line in modified_array:
                #print(line)
            #print("---------------------------------")
            steps = 0
            while(move_check_for_loop(modified_array) is not False and steps < 10000):
                #print(f"curr location is {CURR_LOCATION_Y} and {CURR_LOCATION_X}")
                steps += 1
            if steps >= 10000:
                DETECTED_LOOPS += 1
            #print(f"steps taken is {steps}")
print(DETECTED_LOOPS)

