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

my_answ = 0
for item in numbers:
    my_num = int(item)
    for i in range(0, 2000):
        my_num = evolve(my_num)
    my_answ += my_num
print(my_answ)
