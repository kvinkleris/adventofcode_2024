import sys
from heapq import heappush as hpush, heappop as hpop
from collections import defaultdict as dd
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
file_to_write = open("file_to_write.txt", "w")

def adjs(input_tuple):
    if input_tuple not in cache:
        target, a1, a2, a3 = input_tuple

        if len(target) == 0:
            return 0

        # Try all possible moves and find the minimum
        for posskey in mapping2.values():

            if posskey == "A":
                a3action = mapping2[a3]
                if a3action == "A":
                    a2action = mapping2[a2]
                    if a2action == "A":
                        a1key = mapping[a1]
                        if a1key == target[0]:
                            # Successfully pressed target character
                            yield 1, (target[1:], a1, a2, a3)
                        else:
                             pass
                    else:
                        # a2 moves a1
                        newa1 = move(a1, a2action)
                        if newa1 in mapping.keys():
                            yield 1, (target, newa1, a2, a3)
                        else:
                            pass
                else:
                    # a3 moves a2
                    newa2 = move(a2, a3action)
                    if newa2 in mapping2.keys():
                        yield 1, (target, a1, newa2, a3)
                    else:
                        pass
            else:
                # Move a3
                newa3 = move(a3, posskey)
                if newa3 in mapping2.keys():
                    yield 1, (target, a1, a2, newa3)
                else:
                    pass

def sol(c):
    start = (c, m1T["A"], m2T["A"], m2T["A"])
    pq = []
    hpush(pq, (0, start))  # (cost, state
    dists =  dd(lambda: float('inf'))
    dists[start] = 0
    while len(pq) > 0:
        dist, cur = hpop(pq)
        if len(cur[0]) == 0:
            print(f"Reached target with steps: {cur[1]}\n")
            return dist
        for d, adj in adjs(cur):
            if dist + d < dists[adj]:
                dists[adj] = dist + d
                hpush(pq, (dists[adj], adj))

final_answ = 0
for c in file_lines:
    sval = sol(c)
    print(f"Code: {c}, Min moves: {sval}\n")
    print((int(c[:-1]), c[1:]))
    final_answ += sval * int(c[:-1])

print(f"final_answ: {final_answ}\n")

file_to_write.close()