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
            (1,1) : "v",
            (1,2) : ">",}

movement_map = {"^": (-1, 0),  "<": (0, -1), "v": (1, 0), ">": (0, 1)}

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
                            yield 1, posskey, (target[1:], a1, a2, a3)
                        else:
                             pass
                    else:
                        # a2 moves a1
                        newa1 = move(a1, a2action)
                        if newa1 in mapping.keys():
                            yield 1, posskey, (target, newa1, a2, a3)
                        else:
                            pass
                else:
                    # a3 moves a2
                    newa2 = move(a2, a3action)
                    if newa2 in mapping2.keys():
                        yield 1, posskey,(target, a1, newa2, a3)
                    else:
                        pass
            else:
                # Move a3
                newa3 = move(a3, posskey)
                if newa3 in mapping2.keys():
                    yield 1, posskey,(target, a1, a2, newa3)
                else:
                    pass

# def sol(c):
#     start = (c, m1T["A"], m2T["A"], m2T["A"])
#     pq = []
#     hpush(pq, (0, start))  # (cost, state
#     dists =  dd(lambda: float('inf'))
#     dists[start] = 0
#     while len(pq) > 0:
#         dist, cur = hpop(pq)
#         if len(cur[0]) == 0:
#             print(f"Reached target with steps: {cur[1]}\n")
#             return dist
#         for d, b, adj in adjs(cur):
#             if dist + d < dists[adj]:
#                 dists[adj] = dist + d
#                 hpush(pq, (dists[adj], adj))


def solV(c):
    start = (c, m1T["A"], m2T["A"], m2T["A"])
    pq = []
    hpush(pq, (0, start))  # (cost, state
    dists =  dd(lambda: float('inf'))
    dists[start] = 0
    from_ = {}
    while len(pq) > 0:
        dist, cur = hpop(pq)
        if len(cur[0]) == 0:
            b = None
            bs = []
            while cur != start:
                #print(cur, b)
                cur, b = from_[cur]
                bs.append(b)
            return dist
        for d, b, adj in adjs(cur):
            if dist + d < dists[adj]:
                from_[adj] = cur, b
                dists[adj] = dist + d
                hpush(pq, (dists[adj], adj))

def required(sx, sy, ex, ey, gridtype):

    sign = lambda x: (1, -1)[x<0]
    #print(f"Values : {sx} {sy} {ex} {ey}")
    dx = sign(ex-sx)
    dy = sign(ey-sy)
    #print(dx)
    #print(dy)
    xcount = round((ex-sx) / dx) if dx != 0 else 0
    ycount = round((ey-sy) / dy) if dy != 0 else 0
    xvar = "v" if dx == 1 else "^"
    yvar = ">" if dy == 1 else "<"
    if gridtype == 1:
        bad1 = (m1T["7"], m1T["4"], m1T["1"])
        bad2 = (m1T["0"], m1T["A"])
        #yield ycount * yvar + xcount * xvar
        #yield xcount * xvar + ycount * yvar
        if ((sx, sy) in bad1 and (ex,ey) in bad2):
            yield ycount * yvar + xcount * xvar
        elif ((sx, sy) in bad2 and (ex,ey) in bad1):
            yield xcount * xvar + ycount * yvar
        else:
            yield ycount * yvar + xcount * xvar
            yield xcount * xvar + ycount * yvar
    else:
        bad1 = (m2T["<"])
        bad2 = (m2T["^"], m2T["A"])
        if ((sx, sy)) in bad1 and (ex, ey) in bad2:
            yield ycount * yvar + xcount * xvar
        elif ((sx, sy)) in bad2 and (ex, ey) in bad1:
            yield xcount * xvar + ycount * yvar
        else:
            yield ycount * yvar + xcount * xvar
            yield xcount * xvar + ycount * yvar



#print(required(*m1T['9'], *m1T['A'], 1))

def solve(seq, n, maxn, depth = 0):
    #print(f" depth is {depth}  call is {seq} and n is {n}")
    if n == 0:
        return len(seq)
    if (seq, n, maxn) not in cache:
        cur = "A"
        m = mapping if n == maxn else mapping2
        mT = m1T if n == maxn else m2T
        mtype = 1 if n == maxn else 2
        count = 0
        for des in seq + ("A" if n != maxn else ""):
            bestway = None
            for way in required(*mT[cur], *mT[des], mtype):
                if bestway is None:
                    bestway = solve(way, n-1, maxn, depth = depth + 1)
                else:
                    bestway = min(bestway, solve(way, n-1, maxn, depth = depth + 1))
            count += bestway
            if n == 1:
                count += 1
            cur = des
        cache[seq, n, maxn] = count
    #print(f" answer :  {depth}-> {cache[seq, n, maxn]}")
    return cache[seq, n, maxn]

print(solve("029A", 3, 3, 0))
#print(solV("0"))

final_answ = 0
for c in file_lines:
    sval = solve(c, 26, 26, 0)
    #sval2 = solV(c)
    print((int(c[:-1]), c))
    final_answ += sval * int(c[:-1])

print(f"final_answ: {final_answ}\n")

file_to_write.close()