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

memoization_dict = {}
def DFS(curr_word, goal_word, answ, prev_word):
    """Find all possible word combos"""
    curr_word = curr_word.replace(" ", "")

    if (len(curr_word) > 0) and curr_word != goal_word[:len(curr_word)]:
        #print("return 0")
        return 0
    if curr_word == goal_word:
        #print("return 1")
        memoization_dict[prev_word] = {"next_word" : curr_word}
        return 1
    memoization_dict[prev_word] = {"next_word" : curr_word}
    answ = 0
    for design in DESIGNS:
        if curr_word + design in memoization_dict:
            while True:
                if curr_word + design in memoization_dict:
                    curr_word = memoization_dict[curr_word+design]["next_word"]
                    if curr_word == goal_word:
                        answ += 1
                else:
                    break
        else:
            answ += DFS(curr_word + design, goal_word, answ, curr_word)


    return answ

final_answ = 0
for combo in COMBOS:
        final_answ += DFS("", combo, 0, "")

print(memoization_dict)
print(final_answ)
