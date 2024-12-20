WIDTH = 11
HEIGHT = 7
SECONDS = 1

def load_data():
    """Load data"""
    file = open("robots.txt","r")
    data = file.read().split("\n")
    data_list = []
    for line in data:
        line = line.split(" ")
        split_one = line[0].split(",")
        split_two = line[1].split(",")
        p_x = int(''.join(char for char in split_one[0] if char.isdigit()))
        p_y = int(''.join(char for char in split_one[1] if char.isdigit()))
        v_x = int(''.join(char for char in split_two[0] if char.isdigit()))
        v_y = int(''.join(char for char in split_two[1] if char.isdigit()))
        dict = {}
        dict["P"] = {"x" : p_x, "y" : p_y}
        dict["V"] = {"x" : v_x, "y" : v_y}
        data_list.append(dict)
    return data_list


info_list = load_data()
answ_list = []
print(info_list)
for robot in info_list:
    counter = 0
    while (counter < SECONDS):
        counter += 1
        robot['P']['x'] = (robot['P']['x'] + robot['V']['x']) % WIDTH
        robot['P']['y'] = (robot['P']['y'] + robot['V']['y']) % HEIGHT
        if robot['P']['x'] < 0:
            robot['P']['x'] = WIDTH + robot['P']['x'] - 1
            robot['P']['y'] = HEIGHT + robot['P']['y'] - 1
    answ_list.append(robot)


print(info_list)