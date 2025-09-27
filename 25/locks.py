data = open("locks.txt").read().split("\n\n")

keys = []
locks = []

# Separate keys and locks
for item in data:
    if item[0] == '#':
        locks.append(item.split("\n"))
    else:
        keys.append(item.split("\n"))

# Calculate heights for locks
locks_height = []
for item in locks:
    arr = []
    for i in range(len(item[0])):  # For each column
        count = -1  # Start at -1 to exclude the full row
        for j in range(len(item)):  # For each row
            if item[j][i] == '#':
                count += 1
        arr.append(count)
    locks_height.append(arr)

# Calculate heights for keys
keys_height = []
for item in keys:
    arr = []
    for i in range(len(item[0])):  # For each column
        count = -1  # Start at -1 to exclude the full row
        for j in range(len(item)):  # For each row
            if item[j][i] == '#':
                count += 1
        arr.append(count)
    keys_height.append(arr)

# Check valid key-lock pairs
valid_pairs = 0
max_height = len(locks[0]) - 2  # Total rows minus top and bottom

for key in keys_height:
    for lock in locks_height:
        valid = True
        for i in range(len(lock)):
            if key[i] + lock[i] > max_height:  # Fixed: use max_height instead of len(lock)
                valid = False
                break
        if valid:
            valid_pairs += 1

print(f"Valid key-lock pairs: {valid_pairs}")