"""Advent of code day 2"""

def check_increasing(number_list, depth):
    """check increasing"""

    temp_list = number_list
    if depth >= 2:
        return False
    
    for i in range(0,len(temp_list) - 1):
        if int(temp_list[i]) >= int(temp_list[i + 1]):
            temp_list.pop(i)
            print(temp_list)
            return check_increasing(temp_list, depth + 1)
        if int(temp_list[i + 1]) - int(temp_list[i]) > 3:
            print(temp_list)
            temp_list.pop(i)
            return check_increasing(temp_list, depth + 1)
    return True

def check_decreasing(number_list, depth):
    """check decreasing"""
    temp_list = number_list
    if depth >= 2:
        return False
    for i in range(0, len(temp_list) - 1):
        if int(temp_list[i]) <= int(temp_list[i + 1]):
            temp_list.pop(i)
            print(temp_list)
            return check_decreasing(temp_list, depth + 1)
        if int(temp_list[i]) - int(temp_list[i + 1]) > 3:
            temp_list.pop(i)
            print(temp_list)
            return check_decreasing(temp_list, depth + 1)
    return True


file = open("info.txt", "r")
string = file.read()

string_list = string.split("\n")
#print(list)

item_list = []
for item in string_list:
    item_list.append(item.split(" "))

answ = 0

for item in item_list:
    if check_decreasing(item, 0) or check_increasing(item, 0):
        print(item)
        answ += 1

print(answ)

