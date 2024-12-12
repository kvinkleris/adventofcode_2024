file = open("memory.txt")
info = file.read()

memory_list = []
dict_of_dots = []
counter = 0
block_amount = 0
for index, letter in enumerate(info):
    if index % 2 == 0:
        for i in range(0, (int(letter))):
            memory_list.append(counter)
            block_amount += 1
        counter += 1
    else:
        for i in range(0, ((int(letter)))):
            memory_list.append(".")
            dict_of_dots.insert(0, len(memory_list))


def check_if_fully_formatted(check_list):
    """Checks if disk is fully formatted"""
    dot_found = False
    for index, element in enumerate(check_list):
        if element == '.':
            dot_found = True
        if dot_found is True and element != '.':
            return False
    print("Fully formatted")           
    return True

def format_first_method():
    """format memory string by first method"""
    while (len(dict_of_dots) != 0 and check_if_fully_formatted(memory_list) is not True):
        place_value = dict_of_dots.pop() -1
        for index_j, ele in enumerate(memory_list.copy()[::-1]):
            if ele != '.':
                #print(memory_list)
                memory_list[place_value] = ele
                memory_list[-(index_j + 1)] = '.'
                break
        #print(memory_list)
        #print(len(dict_of_dots))


def insert_into_list(num_to_insert, count_to_insert, index_to_remove):
    """Insert blocks into memory """

    for index_i, ele in enumerate(memory_list):
        if index_i % 1000 == 0:
            print(f"Calculating... {index_i}/{len(memory_list)}")
        if ele == '.':
            space_to_fill = 0
            for index_j, ele_j in enumerate(memory_list[index_i:]):
                if ele_j == '.':
                    space_to_fill += 1
                else:
                    break
            if space_to_fill >= count_to_insert:

                if (index_i < index_to_remove):
                    #print(f"index i {index_i}")
                    #print(f"insert into list {num_to_insert} count to insert {count_to_insert} index_to_remove {index_to_remove} space to fill {space_to_fill}")
                    if (count_to_insert > 1):
                        memory_list[index_i:index_i + count_to_insert] = [num_to_insert] * count_to_insert
                        memory_list[index_to_remove: index_to_remove + count_to_insert + 1] = ['.'] * count_to_insert
                    else:
                        memory_list[index_i] = num_to_insert
                        memory_list[index_to_remove] = '.'
                    #print(memory_list)
                    space_to_fill = 0
                break
        
def format_second_method():
    """Format memory string by second method"""
    dict_of_blocks = {}
    max_value = 0
    for index_j, item in enumerate(memory_list):
        if index_j % 1000 == 0:
            print(f"formatting  {index_j}/{len(memory_list)}")
        if item != '.':
            if int(item) > max_value:
                max_value = int(item)
        if item not in dict_of_blocks and item != '.':
            dict_of_blocks[item] = {"elem_num" : item, "block_size" : 1, "starting_index" : index_j}
        elif item in dict_of_blocks:
            dict_of_blocks[item]["block_size"] = dict_of_blocks[item]["block_size"] + 1
        else:
            continue

    #print(dict_of_blocks)




    for value in range (max_value, 0, -1):
        if value in dict_of_blocks:
            #print(value)
            insert_into_list(dict_of_blocks[value]["elem_num"], dict_of_blocks[value]["block_size"], dict_of_blocks[value]["starting_index"])

    #print(memory_list)


formated_file = open("formated_memory.txt", "w")

answ = 0


format_second_method()
#print(answ)
#formated_file.write(",".join(map(str, memory_list)))
