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

    p1 = 0
    p2 = len(memory_list) - 1
    curr_space_to_insert = 0
    elements_to_insert = 0
    ele_to_insert = memory_list[p2]
    insert_needed = False
    counter = 0
    print(memory_list)
    
    formated_file = open("formated_memory.txt", "w")
    formated_file.write(",".join(map(str, memory_list)))

    prints_file = open("prints_file.txt", "a")
    while p2 >= 0:
        counter += 1
        if insert_needed is True:
            if curr_space_to_insert >= elements_to_insert:
                prints_file.write(f" p1 is : {p1} p2 is {p2} inserting elements start index {p1 - curr_space_to_insert} end index is {p1 - curr_space_to_insert + elements_to_insert} insert ele {ele_to_insert} amount to insert is {elements_to_insert} curr_space_to_insert {curr_space_to_insert} \n")
                memory_list[p1 - curr_space_to_insert : p1 - curr_space_to_insert + elements_to_insert] = [ele_to_insert] * elements_to_insert
                memory_list[p2 +1:p2+ elements_to_insert +1] = ['.'] * elements_to_insert
                #print(memory_list)
                p1 = 0
                insert_needed = False
                ele_to_insert = memory_list[p2]
                elements_to_insert = 0
                curr_space_to_insert = 0

            else:
                if memory_list[p1] == '.':
                    curr_space_to_insert += 1
                    p1 += 1
                else:
                    p1 += 1
                    curr_space_to_insert = 0
                if (p1 > p2 + 1):
                    p1 = 0
                    insert_needed = False
                    ele_to_insert = memory_list[p2]
                    elements_to_insert = 0
                    curr_space_to_insert = 0
        else:
            if memory_list[p2] != '.' and ele_to_insert == memory_list[p2]:
                elements_to_insert += 1
                p2 -= 1
            elif elements_to_insert >= 1:
                insert_needed = True
            else:
                p2 -= 1
                ele_to_insert = memory_list[p2]
        #print(f"{p1} {p2} {elements_to_insert} {insert_needed}")
       #print(memory_list)
        #print(memory_list)

                




answ = 0


format_second_method()
#print(memory_list)
for i in range(0, len(memory_list)):
    if memory_list[i] != '.':
        answ += i * memory_list[i]
print(answ)

    
formated_file = open("answer_memory.txt", "w")
formated_file.write(",".join(map(str, memory_list)))