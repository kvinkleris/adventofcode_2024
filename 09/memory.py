file = open("memory.txt")
info = file.read()

memory_list = []
dict_of_dots = []
counter = 0
for index, letter in enumerate(info):
    if index % 2 == 0:
        for i in range(0, (int(letter))):
            memory_list.append(counter)
        counter += 1
    else:
        for i in range(0, ((int(letter)))):
            memory_list.append(".")
            dict_of_dots.append(len(memory_list))



print(memory_list)
print(dict_of_dots)