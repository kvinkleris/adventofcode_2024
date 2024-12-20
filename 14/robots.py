WIDTH = 101
HEIGHT = 103
SECONDS = 10000

def load_data():
    """Load data"""
    file = open("robots.txt","r")
    data = file.read().split("\n")
    data_list = []
    for line in data:
        line = line.split(" ")
        split_one = line[0].split(",")
        split_two = line[1].split(",")
        p_x = int(''.join(char for char in split_one[0] if char.isdigit() or char == '-'))
        p_y = int(''.join(char for char in split_one[1] if char.isdigit() or char == '-'))
        v_x = int(''.join(char for char in split_two[0] if char.isdigit() or char == '-'))
        v_y = int(''.join(char for char in split_two[1] if char.isdigit() or char == '-'))
        dict = {}
        dict["P"] = {"x" : p_x, "y" : p_y}
        dict["V"] = {"x" : v_x, "y" : v_y}
        data_list.append(dict)
    return data_list


def print_array(data, curr_seconds):

    """print results of iterations to a txt file"""
    answers = open("tree_search.txt","a")
    array = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for temp_robot in data:
        array[temp_robot['P']['y']][temp_robot['P']['x']] ='@'
    if curr_seconds >= 805:
        answers.write(f"RESULT AFTER : {curr_seconds} SECONDS \n")
        for line in array:
            answers.write(" ".join(line) + "\n")
        answers.write("----------------------------------------------\n")

info_list = load_data()
counter = 0
while counter < SECONDS:
    answ_list = []
    counter += 1
    for robot in info_list:
        robot['P']['x'] = (robot['P']['x'] + robot['V']['x']) % (WIDTH )
        robot['P']['y'] = (robot['P']['y'] + robot['V']['y']) % (HEIGHT )
        if robot['P']['x'] < 0:
            robot['P']['x'] = WIDTH + robot['P']['x'] 
            robot['P']['y'] = HEIGHT + robot['P']['y'] 
        #print(robot)
        answ_list.append(robot)
    print_array(answ_list, counter)


    

def calculate_quadrants(x,y):
    """calculate quadrant"""
    mid_x = WIDTH//2
    mid_y = HEIGHT//2
    if x == mid_x:
        return 0
    if y == mid_y:
        return 0
    if x < mid_x and y < mid_y:
        return 1
    if x > mid_x and y < mid_y:
        return 2
    if x < mid_x and y > mid_y:
        return 3
    if x > mid_x and y > mid_y:
        return 4
       
final_answ_dict = {}
for item in answ_list:

    quadrant = calculate_quadrants(item['P']['x'], item['P']['y'])
    if quadrant == 0:
        continue
    if quadrant not in final_answ_dict:
        final_answ_dict[quadrant] = {"answ" : 1}
    else:
        final_answ_dict[quadrant]["answ"] =  final_answ_dict[quadrant]["answ"] + 1

FINAL_ANSW_NUMBER = 1

for item in final_answ_dict.items():
    FINAL_ANSW_NUMBER *= item[1]['answ']
    #FINAL_ANSW_NUMBER *= final_answ_dict["answ"]
print(final_answ_dict)
print(FINAL_ANSW_NUMBER)

