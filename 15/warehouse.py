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
        

def print_map():
    """Print map array"""
    print("--------------------------")
    for line in map_data:
        print(line)
    print("--------------------------")
for move in move_data:
    #print_map()
    coords_tuple = execute_move(move, robot_coords_x, robot_coords_y)
    print(f"returned tuple {coords_tuple}")
    robot_coords_y = coords_tuple[0]
    robot_coords_x = coords_tuple[1]


print(calculate_answer(map_data))
    
