from collections import defaultdict

lines = open("lan_party.txt","r").read().strip().split("\n")

def gen_graph(lines):
    connection_dict = defaultdict(set)  # Use sets instead of lists
    for line in lines:
        if line:  # Skip empty lines
            a, b = line.split("-")
            connection_dict[a].add(b)
            connection_dict[b].add(a)
    return connection_dict

my_dict = gen_graph(lines)
answ = 0
my_sets = []
# Count common neighbors for all pairs
#print(my_dict)
for item in my_dict:
    for item2 in my_dict:
        if item < item2:  # Avoid counting pairs twice
            if item in my_dict[item2] or item2 in my_dict[item]:
                common = my_dict[item] & my_dict[item2]  # Set intersection
                if len(common) == 0:
                    continue
                print(f"{common} is between {item} and {item2}")
                for common_eles in common :
                    #print(f"{item} : {item2} {common}")
                    triangle_set = set()
                    triangle_set.add(item)
                    triangle_set.add(item2)
                    triangle_set.add(common_eles)
                    if item[0] != 't' and item2[0] != 't' and common_eles[0] != 't':
                        break
                    if triangle_set not in my_sets:
                        my_sets.append(triangle_set)

            answ += len(common)
print(len(my_sets))

#print(my_sets)