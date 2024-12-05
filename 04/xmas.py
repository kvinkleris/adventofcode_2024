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



print(FULL_ARRAY)


print(FULL_ANSW)





    



