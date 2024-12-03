"""Advent of code day 2"""

def check_increasing(number_list):
    """check increasing"""

    for i in range(0, len(number_list) - 1):
        if int(number_list[i]) > int(number_list[i + 1]):
            return False
        if abs(int(number_list[i + 1]) - int(number_list[i])) > 3 or abs(int(number_list[i]) - int(number_list[i + 1])) == 0:
            return False
    return True

def check_decreasing(number_list):
    """check decreasing"""
    for i in range(0, len(number_list) - 1):
        if int(number_list[i]) < int(number_list[i + 1]):
            return False
        if abs(int(number_list[i]) - int(number_list[i + 1])) > 3 or abs(int(number_list[i]) - int(number_list[i + 1])) == 0:
            return False
    return True


file = open("info.txt", "r")
string = file.read()

string_list = string.split("\n")
#print(list)

item_list = []
for item in string_list:
    item_list.append(item.split(" "))

answ = 0
answers = []

for item in item_list:
    #print(item)
    for i in range (0, len(item)):

        item_copy = item[:]
        item_copy.pop(i)
        print(item_copy)

        if check_decreasing(item_copy) or check_increasing(item_copy):
            answ += 1
            answers.append(item)
            print(f" PASS : {item_copy}")
            break

print(answ)

