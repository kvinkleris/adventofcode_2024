from collections import defaultdict

file = open("blinking.txt", "r")

data = [int(x) for x in file.read().split(" ")]

nums = defaultdict(int)
for x in data:
    nums[x] += 1
counter = 0


map_of_answers = {}
def build_answer(nums: dict):
    print(nums)
    new_nums = defaultdict(int)

    for x in nums:
        if x == 0:
            new_nums[x + 1] +=  nums[0]
        elif len(str(x)) % 2 == 0:
            new_nums[int(x // (10 ** (len(str(x)) / 2)))] += nums[x]
            new_nums[int(x % (10 ** (len(str(x)) / 2)))] += nums[x]
        else:
            new_nums[x*2024] += nums[x]
    return new_nums

final_answ = 0

while counter < 75:
    nums = build_answer(nums)
    counter += 1
    
for elem in nums:
    final_answ += nums[elem]
print(final_answ)
