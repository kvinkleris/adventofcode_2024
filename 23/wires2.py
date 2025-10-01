import sys
sys.setrecursionlimit(100000)


with open("inputs.txt") as f:
    s = f.read().strip()


def printc(x):
    pyperclip.copy(x)
    print_(x)

answ = res = 0

# g = [list(r) for r in s.split("\n")]
# n,m = len(g), len(g[0])

# for l in s.split("\n")
#     pass

# printc(ans)

g = {}
inits, gates = s.split("\n\n")
for line in inits.split("\n"):
    a,b = line.split(":")
    b = int(b)
    g[a] = b

gd = {}

for l in gates.split("\n"):
    l = l.split(" ")
    a = l[0]
    op = l[1]
    b = l[2]
    out = l[-1]
    gd[out] = (a,b,op)

gd["z20"],gd["jgb"] = gd["jgb"],gd["z20"]
gd["z24"],gd["vcg"] = gd["vcg"],gd["z24"]
gd["z31"],gd["fqm"] = gd["rvc"],gd["z31"]
 
def filt(ss):
    return {x for x in ss if x.startswith("x") or x.startswith("y") or x.startswith("z")}




def touched(reg):
    ts = set()
    def dfs(reg):
        if reg in ts:
            return
        else:
            ts.add(reg)
            if reg in inits:
                a.add(reg)
                return
            else:
                a,b,op = gd[reg]
                ts.add(a)
                ts.add(b)
                dfs(a)
                dfs(b)
    dfs(reg)
    return 0


def pprint(reg, maxdepth = 5, depth = 0):
    if depth > maxdepth:
        return
    if reg in inits:
        pass
        print(" " * depth + reg)
    else:
        a,b,op = gd[reg]
        print(" " + str(depth) + str(reg) + f" = {op} {a} { b}")
        pprint(a, maxdepth = maxdepth, depth = depth + 1)
        pprint(b, maxdepth = maxdepth, depth = depth + 1)

def evaluate(x = None,y = None):
    gloc = g.copy()

    if x is not None:
        for k in list(g.keys()):
            if k.startswith("x"):
                bitidx = int(k[1:])
                gloc[k] = (x >> bitidx) & 1
    if y is not None:
        for k in list(g.keys()):
            if k.startswith("y"):
                bitidx = int(k[1:])
                gloc[k] = (y >> bitidx) & 1

    def dfs(reg):
        if reg not in gloc:
            a,b,op = gd[reg]
            left = dfs(a)
            right = dfs(b)
            if op == "OR":
                res = left | right
            elif op == "AND":
                res = left & right
            else:
                res = left ^ right
            gloc[reg] = res
        return gloc[reg]

    zouts = {}
    for reg in gd.keys():
        if reg.startswith("z"):
            zouts[reg] = dfs(reg)

    keys = sorted(zouts)[::-1]
    answ = 0

    for k in keys:
        answ <<= 1
        answ |= zouts[k]
    return answ

    not_traversed = []
    for k in gd.keys():
        if k not in gloc:
            nott.append(k)



def inspection():
    for i in range(36):
        for j in range(36):
            x = 1 << i
            y = 1 << j
            if evaluate(x,y) != x + y:
                print(i,j)
#print(evaluate())

#pprint("z13", maxdepth = 3)
#print(evaluate(2,3))
inspection()



def inspection():
    for i in range(45):
        for j in range(45):
            x = 1 << i 
            y = 1 << j
            if evaluate(x,y) != x + y:
                print(i, j)

#pprint("z09")
#print()
#pprint("z20")
#print()
#pprint("z21")
#print()
#pprint("z24")
#print()
#pprint("z25")
pprint("z31")
print()
pprint("z32")
print()
pprint("z05")