from collections import deque

map_file = open("warehouse.txt", "r")
map_data = [list(x) for x in  map_file.read().split("\n")]
move_file = open("moves.txt","r")
move_data = [x for x in move_file.read().replace("\n","")]

robot_coords_x = 0
robot_coords_y = 0
for y_index, row in enumerate(map_data):
    for x_index,ele in enumerate(row):
        if ele == '@':
            robot_coords_x = x_index
            robot_coords_y = y_index

print(f"Robot coordinates are {robot_coords_x} {robot_coords_y}")

def expand_map(old_map):
    new_map = []
    new_x = 0
    new_y = 0

    for index_i, row in enumerate(old_map):
        new_row = []
        for index_j, ele in enumerate(row):
            if ele == '#':
                new_row.append('#')
                new_row.append('#')
            elif ele == '.':
                new_row.append('.')
                new_row.append('.')
            elif ele == 'O':
                new_row.append('[')
                new_row.append(']')
            elif ele == '@':
                new_row.append('@')
                new_row.append('.')
        new_map.append(new_row[:])
        #new_map[new_y][new_x] = '@'

    return new_map

newer_map = expand_map(map_data)
for row in newer_map:
    print(row)


for y_index, row in enumerate(newer_map):
    for x_index,ele in enumerate(row):
        if ele == '@':
            robot_coords_x = x_index
            robot_coords_y = y_index

def calculate_answer(map_data):
    """Calculate distance of O values from map edges"""
    answ = 0
    for index_i, row in enumerate(map_data):
        for index_j, ele in enumerate(row):
            if ele == 'O':
                answ += (index_i * 100) + index_j
    return answ


def execute_move(ele, robot_x, robot_y):
    """execute single_move"""
    print(f"Robot coordinates are {robot_coords_x} {robot_coords_y}")
    print("ele")
    if ele == '>':
        print(f"executing loop 1 ele is {ele}")
        if map_data[robot_y][robot_x + 1] == '#':
            return (robot_y, robot_x)
        elif map_data[robot_y][robot_x + 1] == 'O':
            push_location = robot_x + 2
            while True:
                if map_data[robot_y][push_location] == '#':
                    return (robot_y, robot_x)
                elif map_data[robot_y][push_location] == 'O':
                    push_location += 1
                elif map_data[robot_y][push_location] == '.':
                    map_data[robot_y][robot_x] = '.'
                    map_data[robot_y][robot_x + 1] = '@'
                    map_data[robot_y][push_location] = 'O'
                    return (robot_y, robot_x + 1)

        else:
            map_data[robot_y][robot_x] = '.'
            map_data[robot_y][robot_x + 1] = '@'
            return (robot_y, robot_x + 1)

    if ele == '<':
        print(f'executing loop 2 ele is {ele}')
        if map_data[robot_y][robot_x - 1] == '#':
            return (robot_y, robot_x)
        elif map_data[robot_y][robot_x - 1] == 'O':
            push_location = robot_x - 2
            while True:
                if map_data[robot_y][push_location] == '#':
                    return (robot_y, robot_x)
                elif map_data[robot_y][push_location] == 'O':
                    push_location -= 1
                elif map_data[robot_y][push_location] == '.':
                    map_data[robot_y][robot_x] = '.'
                    map_data[robot_y][robot_x - 1] = '@'
                    map_data[robot_y][push_location] = 'O'
                    return(robot_y, robot_x - 1)
        else:
            map_data[robot_y][robot_x] = '.'
            map_data[robot_y][robot_x - 1] = '@'
            return (robot_y,robot_x - 1)
        
    if ele == '^':
        print(f'executing loop  3 ele is {ele}')
        if map_data[robot_y - 1][robot_x] == '#':
            return (robot_y, robot_x)
        elif map_data[robot_y - 1][robot_x] == 'O':
            push_location = robot_y - 2
            while True:
                print(f"curr evaluated ele is {map_data[push_location][robot_x]} push_location is {push_location} x is {robot_x}")
                if map_data[push_location][robot_x] == '#':
                    return (robot_y, robot_x)
                elif map_data[push_location][robot_x] == 'O':
                    push_location -= 1
                elif map_data[push_location][robot_x] == '.':
                    print(f"curr evaluated ele is {map_data[push_location][robot_x]} push_location is {push_location} x is {robot_x}")        
                    map_data[robot_y][robot_x] = '.'
                    map_data[robot_y - 1][robot_x] = '@'
                    map_data[push_location][robot_x] = 'O'
                    return (robot_y - 1, robot_x)
        else:
            map_data[robot_y][robot_x] = '.'
            map_data[robot_y - 1][robot_x] = '@'
            return (robot_y -1, robot_x)
    if ele == 'v':
        print(f'executing loop 4 ele is {ele}')
        if map_data[robot_y + 1][robot_x] == '#':
            return (robot_y, robot_x)
        elif map_data[robot_y + 1][robot_x] == 'O':
            push_location = robot_y + 2
            while True:
                if map_data[push_location][robot_x] == '#':
                    return (robot_y, robot_x)
                elif map_data[push_location][robot_x] == 'O':
                    push_location += 1
                elif map_data[push_location][robot_x] == '.':
                    map_data[robot_y][robot_x] = '.'
                    map_data[robot_y + 1][robot_x] = '@'
                    map_data[push_location][robot_x] = 'O'
                    return (robot_y + 1, robot_x)
        else:
            map_data[robot_y][robot_x] = '.'
            map_data[robot_y + 1][robot_x] = '@'
            return (robot_y + 1, robot_x)
        

def print_map(map_to_print):
    """Print map array"""
    print("--------------------------")
    for line in map_to_print:
        print(line)
    print("--------------------------")


#for move in move_data:
    #print_map()
    #coords_tuple = execute_move(move, robot_coords_x, robot_coords_y)
    #print(f"returned tuple {coords_tuple}")
    #robot_coords_y = coords_tuple[0]
    #robot_coords_x = coords_tuple[1]

def calculate_two(big_map, pos_x, pos_y):
    """calculate answer of second_item"""
    move_actions = {}
    move_actions["^"] = {"x" : 0, "y" : -1}
    move_actions["v"] = {"x" : 0, "y" : 1}
    move_actions["<"] = {"x" : -1, "y": 0}
    move_actions[">"] = {"x" : +1, "y" : 0}
    for action in move_data:
        #print(action)
        #print(f"Curr position is {pos_y} {pos_x}")
        inc_x = move_actions[action]["x"]
        inc_y = move_actions[action]["y"]
        new_pos_x = pos_x + inc_x
        new_pos_y = pos_y + inc_y
        #print(len(big_map))
        #print(len(big_map[0]))
        #print(f"newer position is {new_pos_y} {new_pos_x}")
        if big_map[new_pos_y][new_pos_x] == '#':
            continue
        elif big_map[new_pos_y][new_pos_x] == '.':
            big_map[new_pos_y][new_pos_x] = '@'
            big_map[pos_y][pos_x] = '.'
            pos_y = new_pos_y
            pos_x = new_pos_x
        elif big_map[new_pos_y][new_pos_x] == 'O' or \
             big_map[new_pos_y][new_pos_x] == '[' or \
             big_map[new_pos_y][new_pos_x] == ']':
                Q = deque()
                if big_map[new_pos_y][new_pos_x] == '[':
                    Q.append((new_pos_y, new_pos_x))
                    Q.append((new_pos_y, new_pos_x +1))
                elif big_map[new_pos_y][new_pos_x] == ']':
                    Q.append((new_pos_y, new_pos_x))
                    Q.append((new_pos_y, new_pos_x - 1))

    
                SEEN = set()
                ok = True
                while Q:
                    #print(f"Q is {Q}")
                    q_ele = Q.popleft()

                    #print(q_ele)
                    old_pos_y = q_ele[0]
                    old_pos_x = q_ele[1]

                    new_pos_x = old_pos_x + inc_x
                    new_pos_y = old_pos_y + inc_y
                    SEEN.add(q_ele)
                    if (new_pos_y, new_pos_x) in SEEN:
                        continue
                    #print(f"new pos y is {new_pos_y} and new_pos_x {new_pos_x}")
                    if big_map[new_pos_y][new_pos_x] == '#':
                        ok = False
                        break
                    if big_map[new_pos_y][new_pos_x] == '[':
                        Q.append((new_pos_y, new_pos_x))
                        Q.append((new_pos_y, new_pos_x +1))
                    if big_map[new_pos_y][new_pos_x] == ']':
                        Q.append((new_pos_y, new_pos_x))
                        Q.append((new_pos_y, new_pos_x - 1))
                    if big_map[new_pos_y][new_pos_x] == 'O':
                        Q.append((new_pos_y, new_pos_x))

                if ok is True:
                    while len(SEEN) > 0:
                        #print(f"SEEN is {SEEN} len is {len(SEEN)}")
                        for item in sorted(SEEN):
                            new_pos_y = item[0] + inc_y
                            new_pos_x = item[1] + inc_x
                            if (new_pos_y, new_pos_x) not in SEEN:
                                big_map[new_pos_y][new_pos_x] = big_map[item[0]][item[1]]
                                big_map[item[0]][item[1]] = '.'
                                SEEN.remove(item)
                                #print(f"SEEN is {SEEN} len is {len(SEEN)}")
                    big_map[pos_y + inc_y][pos_x + inc_x] = '@'
                    big_map[pos_y][pos_x] = '.'
                    pos_y = pos_y + inc_y
                    pos_x = pos_x + inc_x
                    
        #print_map(big_map)    
    return big_map[:]
                    
#print(calculate_answer(map_data))

def calculate_distance_two(answs_map):
    final_number = 0
    for index_i, row in enumerate(answs_map):
        num = 0
        for index_j, square in enumerate(row):
            if square == '[':
                num = 100 * index_i +  index_j
                final_number += num
    return final_number





answ_big_map = calculate_two(newer_map, robot_coords_x, robot_coords_y)

print_map(answ_big_map)

final_answ = calculate_distance_two(answ_big_map)
print(final_answ)