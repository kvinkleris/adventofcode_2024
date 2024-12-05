file = open("info.txt", "r")

info = file.read()

print(info)

letter_set = set()
letter_set.add("X")
letter_set.add("M")
letter_set.add("A")
letter_set.add("S")

letter_stack = []

LETTERS = "XMAS"
LETTERS_BACKWARDS = "SAMX"
FULL_ANSW = 0
FULL_ARRAY = []
for letter in info:
    if letter == "\n":
        FULL_ARRAY.append(letter_stack)
        letter_stack = []
    else:
        letter_stack.append(letter)

def check_horizontal(backwards):
    """Check horizontal"""
    answ = 0
    letters_to_check = []
    if backwards is False:
        letters_to_check = LETTERS[:]
    else:
        letters_to_check = LETTERS_BACKWARDS[:]
    flattened_list = []
    flattened_list = sum(FULL_ARRAY, flattened_list)
    counter = 0
    #print(flattened_list)
    for element in flattened_list:
        if element == letters_to_check[counter]:
            print(letters_to_check[counter])
            counter += 1
            print(counter)
        if counter == 4:
            counter = 0
            answ += 1

    return answ

def check_diagnoal(backwards):
    """Check occurences of xmas diagnonally"""
    answ = 0
    letters_to_check = []
    if backwards is False:
        letters_to_check = LETTERS[:]
    else:
        letters_to_check = LETTERS_BACKWARDS[:]


FULL_ANSW += check_horizontal(True)
FULL_ANSW += check_horizontal(False)



print(FULL_ANSW)
