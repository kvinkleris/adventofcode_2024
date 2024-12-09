file = open("signals.txt", "r")
text = file.read()
lines = text.split("\n")
print(lines)
FULL_ARRAY = [list(line) for line in lines]
print(FULL_ARRAY)

class signal:
    def __init__(self, pos_y, pos_x, symbol):
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.symbol = symbol

dict = {}

for index_i, row in enumerate(FULL_ARRAY):
    for index_j, ele in enumerate(row):
        if ele != '.' or
