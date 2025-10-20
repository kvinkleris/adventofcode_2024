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

def DFS_walls_count(prev_node, letter, y_coords, x_coords, visited: list):
    if ((prev_node, y_coords, x_coords)) in visited:
        #print("visited")
        return []
    
    if x_coords >= LEN_X or x_coords < 0:
        #print(f" prev_node: {prev_node}  coords : {y_coords} - {x_coords}")
        return [(prev_node, y_coords, x_coords)]
    
    if y_coords >= LEN_Y or y_coords < 0:
        #print(f" prev_node: {prev_node}  coords : {y_coords} - {x_coords}")
        return [(prev_node, y_coords, x_coords)]
    
    if data[y_coords][x_coords] != letter:
        #print(f" prev_node: {prev_node}  coords : {y_coords} - {x_coords}")
        return [(prev_node, y_coords, x_coords)]
    
    visited.append((prev_node,y_coords, x_coords))
    
    answ = []
    for result in [
        DFS_walls_count((y_coords, x_coords), letter, y_coords + 1, x_coords, visited),
        DFS_walls_count((y_coords, x_coords), letter, y_coords - 1, x_coords, visited),
        DFS_walls_count((y_coords, x_coords), letter, y_coords, x_coords + 1, visited),
        DFS_walls_count((y_coords, x_coords), letter, y_coords, x_coords - 1, visited)
    ]:
        if result:  # Skip None/empty results
            answ.extend(result)
    
    return answ


# def DFS_corners_count(letter,y_coords, x_coords, visited : list):
#     #for item in data:
#         #print(item)
#     #print("----------------------------")
#     #print(f"{y_coords} {x_coords} ")
#     #print(f"coordinates y :  {y_coords} coordinates x {x_coords}")
    
#     if (y_coords, x_coords) in visited:
#         #print("visited")
#         return 0

#     corners_count = 0
#     if (y_coords, x_coords) in visited:
#         #print("visited")
#         return 0
#     if x_coords >= LEN_X or x_coords < 0:
#         return 0
#     if y_coords >= LEN_Y or y_coords < 0:
#         return 0
#     if data[y_coords][x_coords] != letter:
#         return 0

#     if y_coords > LEN_Y and x_coords > LEN_X:
#         corners_count += 1

#     if y_coords < 0  

#     if data[y_coords + 1][x_coords] > LEN_Y and data[y_coords][x_coords - 1] > LEN_X:
#         corners_count += 1

#     if data[y_coords -1][x_coords] > LEN_Y and data[y_coords][x_coords] > LEN_X:
#         corners_count += 1

#     if data[y_coords + 1][x_coords] > LEN_Y and data[y_coords][x_coords] > LEN_X:
#         corners_count += 1

#     if y_coords >= LEN_Y or y_coords < 0:
#         return 1
#     if data[y_coords][x_coords] != letter:
#         return 1
#     visited.append((y_coords, x_coords))
    

#     #for row in visited:
#     #print(row)
#     #print("--------------------------------------------")
#     answ = 0
#     answ += DFS_corners_count(letter, y_coords + 1, x_coords, visited)
#     answ += DFS_corners_count(letter, y_coords - 1, x_coords, visited)
#     answ += DFS_corners_count(letter , y_coords, x_coords + 1, visited)
#     answ += DFS_corners_count(letter, y_coords , x_coords - 1,  visited)
#     return answ
def calc_part_one():
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
                #print(visited)
                perm_visited = perm_visited + visited[:]


    result = 0
    for item in final_answ:
        result += item[0] * item[1]
    print(result)

def calc_part_two():
    answ = 0
    perm_visited = []
    final_answ = []
    walls = []
    count_walls_final = set()

    for index_i , row in enumerate(data):
        for index_j, ele in enumerate(row):
            #print(perm_visited)
            if (index_i, index_j) not in perm_visited:
                visited = []
                answ = DFS(ele, index_i, index_j, visited)
                #print(visited)
                perm_visited = perm_visited + visited[:]
                visited_walls = []
                walls = DFS_walls_count((index_i, index_j), ele, index_i, index_j, visited_walls)
                
                # Deduplicate walls to count sides
                walls_set = set(walls)
                sides_set = set()
                for p1,p2,p3 in walls_set:
                    keep = True
                    for dy, dx in ((1,0),(0,1)):
                        p1n =  (p1[0] + dy, p1[1] + dx)
                        p2n = (p2 + dy)
                        p3n = (p3 + dx)
                        #print(f"comparing {p1},{p2},{p3} with {p1n} {p2n} {p3n}")
                        if (p1n, p2n, p3n) in walls_set:
                            #print()
                            keep = False
                            break
                            #print("honk")
                    if keep:
                        sides_set.add((p1,p2,p3))
                num_sides = len(sides_set)
                area = len(visited)
                final_answ.append((num_sides, area))
    result = 0
    for sides, area in final_answ:
            result += sides * area
    print(result)


calc_part_two()