file = open("signals.txt", "r")
text = file.read()
lines = text.split("\n")
#print(lines)
FULL_ARRAY = [list(line) for line in lines]
#print(FULL_ARRAY)
LEN_Y = len(FULL_ARRAY)
LEN_X = len(FULL_ARRAY[0])
class signal:
    def __init__(self, pos_y, pos_x, symbol):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.symbol = symbol

dict = {}

for index_i, row in enumerate(FULL_ARRAY):
    for index_j, ele in enumerate(row):
        if ele != '.':
            if ele not in dict:
                print(ele)
                dict[ele] = [(index_i, index_j)]
            else:
                list_of_coords = dict[ele]
                list_of_coords.append((index_i,index_j))

print(LEN_X)
print(LEN_Y)
def calculate_antinode(tuple_list):
    """Place antinodes"""
    for index_i, ele in enumerate(tuple_list[1]):
        for index_j, ele_j in enumerate(tuple_list[1]):
            print(f"{tuple_list[0]} indexes are {index_i} {index_j}")
            if index_i == index_j:
                continue
            FULL_ARRAY[ele[0]][ele[1]] = '#'
            
            diff_y = int(ele[0]) + (int(ele[0]) - int(ele_j[0]))
            diff_x =  int(ele[1]) + (int(ele[1]) - int(ele_j[1]))

            while True:
                if (diff_x >= 0 and diff_x < LEN_X and diff_y >= 0 and diff_y < LEN_Y):
                    FULL_ARRAY[diff_y][diff_x] = '#'
                else:
                    break
                diff_y += (int(ele[0]) - int(ele_j[0]))
                diff_x += (int(ele[1]) - int(ele_j[1]))




            


for symbol in dict.items():
    calculate_antinode(symbol)

for row in FULL_ARRAY:
    print(row)

answ = 0
for index_i, row in enumerate(FULL_ARRAY):
    for index_j, ele in enumerate(row):
        if ele == '#':
            answ += 1

print(answ)




