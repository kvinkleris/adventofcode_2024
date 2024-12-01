file = open("advent_of_code.txt", "r")
string = file.read()

list = string.split("\n")

left_list = []
right_list = []

for item in list:
    temp_list = item.split("   ")
    left_list.append(temp_list[0])
    right_list.append(temp_list[1])


def calculate_distance():
    answ = 0
    left_list = sorted(left_list)
    right_list = sorted(right_list)
    for i in range(0, len(left_list)):
        answ += abs(int(left_list[i]) - int(right_list[i]))

    print(answ)

def calculate_similarity():

    global left_list
    global right_list
    answ_dict = {}
    answ = 0
    left_list = set(left_list)
    for item in right_list:
        if item in answ_dict:
            answ_dict[item]["count"] = answ_dict[item]["count"] + 1
        else:
            answ_dict[item] = {"count" : 1}
    for item_in_set in left_list:
        if item_in_set in answ_dict:
            answ += answ_dict[item_in_set]["count"] * int(item_in_set)

    print(answ)
        
calculate_similarity()



