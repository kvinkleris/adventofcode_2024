file = open("garden_groups.txt", "r")

data = [list(x) for x in file.read().split("\n")]
print(data)
letter_set = set()
for row in data:
    for letter in row:
        letter_set.add(letter)
print(letter_set)
#print(letter_set)

#DFS(letter, x_coords, y_coords):

LEN_Y = len(data)
LEN_X = len(data[0])
def DFS(letter,y_coords, x_coords,answ,  visited : list):
    for item in data:
        print(item)
    print("----------------------------")
    print(answ)
    print(f"coordinates y :  {y_coords} coordinates x {x_coords}")
    if (y_coords, x_coords) in visited:
        return 0
    if x_coords >= LEN_X or x_coords < 0:
        return  1
    if y_coords >= LEN_Y or y_coords < 0:
        return 1
    if data[y_coords][x_coords] != letter:
        return  1
    visited.append((y_coords, x_coords))

    
    answ += DFS(letter, y_coords + 1, x_coords, answ, visited)
    answ += DFS(letter, y_coords - 1, x_coords, answ, visited)
    answ += DFS(letter , y_coords, x_coords + 1, answ, visited)
    answ += DFS(letter, y_coords , x_coords - 1, answ, visited)
    return answ

visited = []
for index_i, row in enumerate(data):
    for index_j, ele in enumerate(row):
        if ele != '.':
            answ = DFS(ele, index_i, index_j, 0, visited)
            print(answ)
    
    
    

