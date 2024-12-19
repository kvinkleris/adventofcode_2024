import regex

file = open("cramers_rule.txt")
data = file.read().split("\n")
def load_values():
    """Parse input data"""
    counter = 0
    list_of_dicts = []
    new_dict = {}
    for line in data:

        if (len(line) == 0):
            continue

        numbers = line.split(",")

        #print(numbers)
        number_x = ''.join(char for char in numbers[0] if char.isdigit())
        number_y = ''.join(char for char in numbers[1] if char.isdigit())
        if counter == 0:
            new_dict["A"] = {"X" : int(number_x), "Y": int(number_y)}
        
        elif counter == 1:
            new_dict["B"] = {"X" : int(number_x), "Y": int(number_y)}
        
        elif counter == 2:
            answ_x = int(number_x) + int(10000000000000)
            answ_y = int(number_y) + int(10000000000000)
            new_dict["ANSW"] = {"X" :answ_x , "Y": answ_y}
        else:
            continue
        counter += 1
        if (counter >= 3):
            list_of_dicts.append(new_dict)
            new_dict = {}
            counter = 0

    return list_of_dicts


def solve(equation_data: dict):
    #print(equation_data)
    """Math equation to solve problem"""
    determinant = equation_data["A"]["X"] * equation_data["B"]["Y"] - equation_data["A"]["Y"] * equation_data["B"]["X"]
    determinant_x1 = equation_data["ANSW"]["X"] * equation_data["B"]["Y"] - equation_data["ANSW"]["Y"] * equation_data["B"]["X"]
    determinant_x2 = equation_data["A"]["X"] * equation_data["ANSW"]["Y"] - equation_data["A"]["Y"] * equation_data["ANSW"]["X"]

    answ_x = determinant_x1 / determinant
    answ_y = determinant_x2 / determinant
    #print(f"answer is {answ_x} and {answ_y}")
    if (answ_x).is_integer() is not True:
        return (0,0)
    if (answ_y).is_integer() is not True:
        return (0,0)
    
    if answ_x * equation_data["A"]["X"] + answ_y * equation_data ["B"]["X"] != equation_data["ANSW"]["X"]:
        #print("something went wrong")
        return (0,0)
    if answ_x * equation_data["A"]["Y"] + answ_y * equation_data ["B"]["Y"] != equation_data["ANSW"]["Y"]:
        #print('something went wrong 2')
        return (0,0)
    
        

    return (answ_x, answ_y)



data_dicts = load_values()
answers = 0
for data_dict in data_dicts:
    tuple_answ = solve(data_dict)
    answers += (tuple_answ[0] * 3) + tuple_answ[1]

print(answers)
    

