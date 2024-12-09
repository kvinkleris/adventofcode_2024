import itertools

file = open("bridge.txt")
text = file.read()
lines = text.split("\n")
results = []
values = []

for line in lines:
    temp_result = line.split(":")
    results.append(temp_result[0])
    values.append(temp_result[1][1:].split(" "))

def concanetate(str1, str2):
    """Concanteate two strings"""
    return (str1 + str2)
def calculate_result():
    FINAL_RESULT = 0
    counter = 0
    for item in values:
        #print(len(item))
        perms = list(itertools.product("+*|", repeat = len(item) - 1 ))
        for perm in perms:
            op_counter = 0
            answ = int(item[op_counter])
            for operation in perm:
                if operation == "+":
                    answ +=  int(item[op_counter+1])
                if operation == "*":
                    answ *=  int(item[op_counter+1])
                if operation == "|":
                    answ = int(concanetate(str(answ), str(item[op_counter+1])))
                op_counter += 1 
            if answ == int(results[counter]):
                FINAL_RESULT += answ
                break
        counter += 1
    return FINAL_RESULT
print(calculate_result())
        


