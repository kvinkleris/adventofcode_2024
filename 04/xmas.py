file = open("info.txt", "r")

info = file.read()

#print(info)

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

    for i, row in enumerate(FULL_ARRAY):
         for j, _ in enumerate(row[:-3]):
            if (FULL_ARRAY[i][j] == letters_to_check[0] and
                FULL_ARRAY[i][j+1] == letters_to_check[1] and
                FULL_ARRAY[i][j+2] == letters_to_check[2] and
                FULL_ARRAY[i][j+3] == letters_to_check[3]):

                    #print(f"HORIZONTAL {i} {j}  {FULL_ARRAY[i][j]} {FULL_ARRAY[i][j+1]} {FULL_ARRAY[i][j+2]} {FULL_ARRAY[i][j+3]}")
                    answ += 1
         #print("")

    return answ

def check_diagonal(backwards, word):
    """Check occurences of xmas diagnonally"""
    answ = 0
    letters_to_check = []
    if backwards is False:
        letters_to_check = word[:]
    else:
        letters_to_check = word[::-1]
    for i, row in enumerate(FULL_ARRAY[:-3]):
        for j, _ in enumerate(row[:-3]):  # -3 since we check 4 consecutive elements
            if (FULL_ARRAY[i][j] == letters_to_check[0] and
                FULL_ARRAY[i+1][j+1] == letters_to_check[1] and
                FULL_ARRAY[i+2][j+2] == letters_to_check[2] and
                FULL_ARRAY[i+3][j+3] == letters_to_check[3]):
                answ += 1
    reversed_array = []
    for item in FULL_ARRAY:
        reversed_array.append(item[::-1])

    for i, row in enumerate((reversed_array[:-3])):
        for j, _ in enumerate(row[:-3]):  # -3 since we check 4 consecutive elements
            if (reversed_array[i][j] == letters_to_check[0] and
                reversed_array[i+1][j+1] == letters_to_check[1] and
                reversed_array[i+2][j+2] == letters_to_check[2] and
                reversed_array[i+3][j+3] == letters_to_check[3]):
                answ += 1
    
    return answ

def compare_arrays(array_to_compare):
    array1 = [[ 'M' ,'.', 'M'],
              ['.', 'A', '.' ],
              ['S', '.', 'S' ]]
    
    array2 = [[ 'M' ,'.', 'S'],
              ['.', 'A', '.' ],
              ['M', '.', 'S' ]]
    
    array3 = [[ 'S' ,'.', 'S'],
              ['.', 'A', '.' ],
              ['M', '.', 'M' ]]
    array4 = [[ 'S' ,'.', 'M'],
              ['.', 'A', '.' ],
              ['S', '.', 'M' ]]
    arrays = []
    arrays.append(array1)
    arrays.append(array2)
    arrays.append(array3)
    arrays.append(array4)

    for array in arrays:
        if (array[0][0] == array_to_compare[0][0] and 
            array[0][2] == array_to_compare[0][2] and
            array[1][1] == array_to_compare[1][1] and
            array[2][0] == array_to_compare[2][0] and
            array[2][2] == array_to_compare[2][2]):
            return True
        
    return False
    

def check_diagonal_cross():
    """Check occurence of X for xmas"""
    
    answ = 0
    for i, row in enumerate(FULL_ARRAY[:-2]):
        for j, _ in enumerate(row[:-2]):  # -3 since we check 4 consecutive elements
            array_to_be_compared = []
            array_to_be_compared.append(FULL_ARRAY[i][j:j+3])
            array_to_be_compared.append(FULL_ARRAY[i+1][j:j+3])
            array_to_be_compared.append(FULL_ARRAY[i+2][j:j+3])
            if compare_arrays(array_to_be_compared):
             answ += 1

    return answ

            

    

    return 0

def check_vertical(backwards):
    """Check occurences of xmas diagnonally"""
    answ = 0
    letters_to_check = []
    if backwards is False:
        letters_to_check = LETTERS[:]
    else:
        letters_to_check = LETTERS_BACKWARDS[:]
    for i, row in enumerate(FULL_ARRAY[:-3]):
        for j, _ in enumerate(row):  # -3 since we check 4 consecutive elements
            if (FULL_ARRAY[i][j] == letters_to_check[0] and
                FULL_ARRAY[i+1][j] == letters_to_check[1] and
                FULL_ARRAY[i+2][j] == letters_to_check[2] and
                FULL_ARRAY[i+3][j] == letters_to_check[3]):
                    answ += 1


    return answ








FULL_ANSW += check_horizontal(True)
FULL_ANSW += check_horizontal(False)

FULL_ANSW += check_diagonal(False, LETTERS)
FULL_ANSW += check_diagonal(True, LETTERS)

FULL_ANSW += check_vertical(True)
FULL_ANSW += check_vertical(False)





print(FULL_ANSW)
print(check_diagonal_cross())
