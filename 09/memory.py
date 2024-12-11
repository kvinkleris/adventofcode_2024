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
    for index, item in enumerate(dict_of_dots):
        block_size = 0
        if (abs(int(last_item) - int(item)) == 1):
            block_size += 1
        else:
            block_size = 0
        if block_size + 1 >= count_to_insert:
            memory_list[index:index+block_size] = count_to_insert
            memory_list[index_to_remove:index_to_remove+block_size] = '.'
            break
        last_item = item

        
        
def format_second_method():
    """Format memory string by second method"""
    old_element = '.'
    for index_j, _ in enumerate(memory_list):
        if memory_list[-(index_j + 1)] != '.':
            if old_element != memory_list[-(index_j + 1)]:
                old_element = memory_list[-(index_j + 1)]
                block_counter = 0
            block_counter += 1

            print(f"{old_element} {block_counter}")
    

formated_file = open("formated_memory.txt", "w")

answ = 0


format_second_method()
#print(answ)
#formated_file.write(",".join(map(str, memory_list)))
