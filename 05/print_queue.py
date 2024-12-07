file1 = open("section1.txt")
file2 = open("section2.txt")

data = file1.read()
info = file2.read()

file1.close()
file2.close()

dict = {}
for item in data.split("\n"):
    split_data = item.split("|")
    #print(split_data)
    if split_data[0] not in dict:
        array = []
        array.append(split_data[1])
        dict[split_data[0]] = {"rules" : array}
        
    else:
       array = dict[split_data[0]]["rules"]
       array.append(split_data[1])

info = info.split("\n")

updates = []
for line in info:
    updates.append(line.split(","))




def check_if_update_correct(update_rules, update):
    """Check if sequence is valid"""
    update_queue = []
    for item in update:
        if item not in update_rules:
            update_queue.append(item)
            continue
        item_check_rules = update_rules[item]['rules']
        for check in item_check_rules:
            if check in update_queue:
                return False
        update_queue.append(item)
    return True
    
def fix_ordering(update_rules, update):
    """Fix ordering"""
    new_line = []
    count = 0
    items_left_to_add = update[:]
    while (len(items_left_to_add) > 0 and count < 500):
        print(len(items_left_to_add))
        print(count)
        for index, ele in enumerate(items_left_to_add):
            can_add = True
            for _, item_two in enumerate(items_left_to_add):
                #print(update_rules)
                if item_two not in update_rules:
                    continue
                if ele in update_rules[item_two]['rules']:
                    #print(f"ele 1 is {ele}, ele two is {item_two} , rules are :  {update_rules[item_two]['rules']}")
                    can_add = False
                    break
            if can_add is True:
                new_item = items_left_to_add.pop(index)
                new_line.append(new_item)
                #print(new_item)
        count += 1
    #print(new_line)
    return new_line
            



            


    #while (check_if_update_correct(update_rules, update) is False):










for line in updates.copy():
    if check_if_update_correct(dict, line) is True:
        updates.remove(line)

new_lines = []
for line in updates.copy():
    new_lines.append(fix_ordering(dict, line))

#print(dict)
answ = 0
for array in new_lines:
    answ += int(array[len(array) // 2])

print(answ)

