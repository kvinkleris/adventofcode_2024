file = open("blinking.txt", "r")

data = [int(x) for x in file.read().split(" ")]
print(data)

counter = 0
new_data = []


map_of_answers = {}
def recursive_search(depth, answ, i, og):
    if depth == 75:
        return answ

    if (answ[i] == 0):
        answ[i] = 1
        recursive_search(depth+1,answ, i, answ[i])
    elif len(str(answ[i])) % 2 == 0:
        temp = answ[i]
        answ[i] = int(temp // (10 ** ((len(str(temp))) // 2)))
        answ.insert(i+1, int(temp % ((10 ** ((len(str(temp))) // 2)))))
        recursive_search(depth+1,answ, i + 1, answ[i+1])
        recursive_search(depth+1,answ, i, answ[i])
        
    else:
        answ[i] = answ[i] * 2024
        recursive_search(depth+1, answ, i, answ[i])
    return answ


print(data)
answ = []
for i in data:
    answ.append(recursive_search(0, [i], 0))
final_answ = 0
for item in answ:
    final_answ += len(item)

    
print(final_answ)