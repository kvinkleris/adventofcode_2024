"""Advent of code day 19"""

from collections import Counter
from functools import cache
def read_files():
    """Read data from files"""
    file1 = open("linen_input.txt")
    designs = [x for x in file1.read().split(",")]
    file1.close()
    file2 = open("combos.txt")
    combos = [x for x in file2.read().split("\n")]
    return designs, combos


DESIGNS, COMBOS = read_files()
DP = {}
def DFS(goal_word):
    """Find all possible word combos"""
    if goal_word in DP:
        return DP[goal_word]
    answ = 0
    if len(goal_word) == 0:
        return 1
   
    
    for design in DESIGNS:
        design = design.replace(" ", "")
        if goal_word[:len(design)] == design:
            answ += DFS(goal_word[len(design):])
  
    DP[goal_word] = answ
    return answ


final_answ = 0

for combo in COMBOS:
    final_answ += DFS(combo)
print(DP)
print(final_answ)
