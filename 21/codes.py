import sys

file_lines = open("data.txt","r").read().split("\n")
#print(file_lines)

mapping = {(0,0) : '7',
           (0,1) : '8',
           (0,2) : '9',
           (1,0) : '4',
           (1,1) : '5',
           (1,2) : '6',
           (2,0) : '1',
           (2,1) : '2',
           (2,2) : '3',
           (3,1) : '0',
           (3,2) : 'A'}

m1T = {v:k for k, v in mapping.items()}

mapping2 = {(0,1) : "^",
            (0,2) : "A",
            (1,0) : "<",
            (1,1) : "⌄",
            (1,2) : ">",}

movement_map = {"^": (-1, 0),  "<": (0, -1), "⌄": (1, 0), ">": (0, 1)}

m2T = {v:k for k, v in mapping2.items()}

def move(pos, dr):
    if dr in movement_map:
        dx, dy = movement_map[dr]
        return (pos[0] + dx, pos[1] + dy)
    return pos

cache = {}
def adj(input_tuple):
    if input_tuple not in cache:
        target, a1, a2, a3 = input_tuple

        if len(target) == 0:
            print(f"Reached target with {input_tuple}")
            #p#rint(result)
            return 0

       
            
        result = float('inf')  # Use infinity instead of large number
        cache[input_tuple] = result
        #print(input_tuple)
        #print(target,a1,a2,a3)
        for posskey in mapping2.values():
            if posskey == "A":
                a3action = mapping2[a3]
                if a3action == "A":
                    a2action = mapping2[a2]
                    if a2action == "A":
                        a1key = mapping[a1]
                        #print(f"{a1key} and {target[0]} ")
                        if a1key == target[0]:
                            #print(f"{a1key} and {target[0]}  are the same... moving to next target")
                            result = min(result, 1 + solve((target[1:], a1, a2, a3)))

                        # else: do nothing (invalid move)
                    else:
                        newa1 = move(a1, a2action)
                        if newa1 in mapping.keys():
                            result = min(result, 1 + solve((target, newa1, a2, a3)))
                        # else: do nothing (invalid move)
                else:
                    newa2 = move(a2, a3action)
                    if newa2 in mapping2.keys():
                        result = min(result, 1 + solve((target, a1, newa2, a3)))
                    # else: do nothing (invalid move)
            else:
                newa3 = move(a3, posskey)
                if newa3 in mapping2.keys():
                    result = min(result, 1 + solve((target, a1, a2, newa3)))
                    
                # else: do nothing (invalid move)
        
        cache[input_tuple] = result
        #print(f"Cache updated for {input_tuple}: {result}")
    return cache[input_tuple]

# Process each line from the file
res = 0
for c in file_lines:
    if c.strip():  # Skip empty lines
        cache.clear()
        res_two = solve((c, m1T["A"], m2T["A"], m2T["A"]))
        print(res_two)
        res+= int(c[:-1]) * res_two
print(res)