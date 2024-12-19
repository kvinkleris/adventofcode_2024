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
def DFS(letter,y_coords, x_coords, visited : list):
    #for item in data:
        #print(item)
    #print("----------------------------")
    #print(f"{y_coords} {x_coords} ")
    #print(f"coordinates y :  {y_coords} coordinates x {x_coords}")
    
    if (y_coords, x_coords) in visited:
        #print("visited")
        return 0
        
    if x_coords >= LEN_X or x_coords < 0:
        return 1
    if y_coords >= LEN_Y or y_coords < 0:
        return 1
    if data[y_coords][x_coords] != letter:
        return 1
    visited.append((y_coords, x_coords))
    

    #for row in visited:
    #print(row)
    #print("--------------------------------------------")
    answ = 0
    answ += DFS(letter, y_coords + 1, x_coords, visited)
    answ += DFS(letter, y_coords - 1, x_coords, visited)
    answ += DFS(letter , y_coords, x_coords + 1, visited)
    answ += DFS(letter, y_coords , x_coords - 1,  visited)
    return answ

def DFS_corners_count(letter,y_coords, x_coords, visited : list):
    #for item in data:
        #print(item)
    #print("----------------------------")
    #print(f"{y_coords} {x_coords} ")
    #print(f"coordinates y :  {y_coords} coordinates x {x_coords}")
    
    if (y_coords, x_coords) in visited:
        #print("visited")
        return 0

    corners_count = 0
    if (y_coords, x_coords) in visited:
        #print("visited")
        return 0
    if x_coords >= LEN_X or x_coords < 0:
        return 0
    if y_coords >= LEN_Y or y_coords < 0:
        return 0
    if data[y_coords][x_coords] != letter:
        return 0
        
    if data[y_coords + 1][x_coords] > LEN_Y and data[y_coords][x_coords + 1] > LEN_X:
        corners_count += 1

    if data[y_coords + 1][x_coords] > LEN_Y and data[y_coords][x_coords - 1] > LEN_X:
        corners_count += 1

    if data[y_coords -1][x_coords] > LEN_Y and data[y_coords][x_coords] > LEN_X:
        corners_count += 1

    if data[y_coords + 1][x_coords] > LEN_Y and data[y_coords][x_coords] > LEN_X:
        corners_count += 1






    if y_coords >= LEN_Y or y_coords < 0:
        return 1
    if data[y_coords][x_coords] != letter:
        return 1
    visited.append((y_coords, x_coords))
    

    #for row in visited:
    #print(row)
    #print("--------------------------------------------")
    answ = 0
    answ += DFS(letter, y_coords + 1, x_coords, visited)
    answ += DFS(letter, y_coords - 1, x_coords, visited)
    answ += DFS(letter , y_coords, x_coords + 1, visited)
    answ += DFS(letter, y_coords , x_coords - 1,  visited)
    return answ

answ = 0
perm_visited = []
final_answ = []
for index_i , row in enumerate(data):
    for index_j, ele in enumerate(row):
        #print(perm_visited)
        if (index_i, index_j) not in perm_visited:
            visited = []
            answ = DFS(ele, index_i, index_j, visited)
            final_answ.append((answ, len(visited)))
            print(visited)
            perm_visited = perm_visited + visited[:]


result = 0
for item in final_answ:
    result += item[0] * item[1]
print(result)

