import re

file = open("info.txt","r")

string = file.read()
pattern = r"""mul\(\d+,\d+\)"""

text = ''.join([i if ord(i) < 128 else ' ' for i in string])

number_pattern = r"""\d+"""
answers = re.findall(pattern, text)
answ = 0
for item in answers:
    numbers = re.findall(number_pattern, item)
    answ += int(numbers[0]) * int(numbers[1])
print(answ)