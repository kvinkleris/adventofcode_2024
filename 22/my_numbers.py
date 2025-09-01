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

def generate_sequences(seqs):
    sequences = set()
    for seq in seqs:
        for x in range(0, len(seq) - 3):
            sequences.add(tuple((seq[x][1],seq[x+1][1], seq[x+2][1], seq[x+3][1])))
            #print(my_tuple)
            #sequences.add(my_tuple)
    return sequences

hash_map = {}
my_answ = 0
all_seqs = set()
for item in numbers:
    hash_map[item] = {}
    seq = []
    my_num = int(item)
    old_num = my_num % 10
    #print(old_num)
    sliding_window = []
    for i in range(0, 2000):
        old_num = my_num
        my_num = evolve(my_num)
        sliding_window.append(my_num % 10 - old_num % 10)
        if len(sliding_window) == 4:
            all_seqs.add(tuple(sliding_window))
            if tuple(sliding_window) not in hash_map[item]:
                hash_map[item] |= {tuple(sliding_window) : my_num % 10}
            sliding_window.pop(0)
        if len(sliding_window) > 4:
            print("FATAL ERROR")
            quit()

best = 0
best_seq = tuple()
for sequence in all_seqs:
    my_sum = 0
    for h_map_key in hash_map:
        if sequence in hash_map[h_map_key]:
            my_sum += hash_map[h_map_key][sequence]
    if my_sum > best:
        best_seq = sequence
        best = my_sum

print(best_seq)
print(best)