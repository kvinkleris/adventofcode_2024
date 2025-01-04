"""Advent of code day 19"""

def read_files():
    """Read data from files"""
    file1 = open("linen_input.txt")
    designs = [x for x in file1.read().split(",")]
    file1.close()
    file2 = open("combos.txt")
    combos = [x for x in file2.read().split("\n")]
    return designs, combos


DESIGNS, COMBOS = read_files()


def DFS(curr_word, goal_word, answ):
    """Find all possible word combos"""
    curr_word = curr_word.replace(" ", "")

    if (len(curr_word) > 0) and curr_word != goal_word[:len(curr_word)]:
        #print("return 0")
        return 0
    if curr_word == goal_word:
        #print("return 1")
        return 1
    answ = 0
    for design in DESIGNS:
        answ += DFS(curr_word + design, goal_word, answ)
    return answ

final_answ = 0
for combo in COMBOS:
    final_answ += DFS("", combo, 0)
print(final_answ)

