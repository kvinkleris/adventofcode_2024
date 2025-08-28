import math

numbers = open("numbers.txt","r").read().split("\n")

def mix(secret_number, value):
    return value ^ secret_number

def prune(secret_num):
    return secret_num & 0b111111111111111111111111

def evolve(secret_num):
    value = secret_num << 6
    secret_num = mix(secret_num, value)
    secret_num = prune(secret_num)

    value = secret_num >> 5
    secret_num = mix(secret_num, value)
    secret_num = prune(secret_num)

    value = secret_num << 11
    secret_num = mix(secret_num, value)
    secret_num = prune(secret_num)
    return secret_num

# my_answ = 0
# for item in numbers:
#      my_num = int(item)
#      for i in range(0, 2000):
#          my_num = evolve(my_num)
#      my_answ += my_num
# my_num = 123

# print(my_answ)

seqs = []
my_answ = 0
possible_sequences = {} 
for item in numbers:
  
    nums = []
    my_num = int(item)
    old_num = my_num % 10
    #print(old_num)
    for i in range(0, 2000):
        old_num = my_num % 10
        my_num = evolve(my_num)
        nums.append(old_num - my_num % 10)
    already_seen = False
    for i in range (0, len(nums) - 3):
        if not item in possible_sequences:
            possible_sequences[item] = {}
        if not (nums[i], nums[i+1],nums[i+2], nums[i+3]) in possible_sequences[item]:
            possible_sequences[item] = possible_sequences[item] | { (nums[i], nums[i+1],nums[i+2], nums[i+3]) : nums[i+3]}
        elif possible_sequences[item][(nums[i], nums[i+1],nums[i+2], nums[i+3])] in possible_sequences[item]:
            possible_sequences[item][(nums[i], nums[i+1],nums[i+2], nums[i+3])] += nums[i+3]
    #print(seq)
print(possible_sequences)

best = 0
#print(set_of_sequences)

print(best)
#print(seqs)
# for sequence in set_of_sequences:
#     curr_money = 0
#     for seq in seqs:
#         for i in range(0, len(seq) - 3):
#             if sequence == tuple((seq[i][1], seq[i+1][1], seq[i+2][1], seq[i+3][1])):
#                 curr_money += seq[i+3][0] % 10
#                 break
#if best < curr_money:
 #       best = curr_money
#print(best)