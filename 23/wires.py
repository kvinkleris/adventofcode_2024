import re

wires = open("wire_data.txt","r").read().strip().split("\n")
wires_two = open("wire_data_two.txt","r").read().strip().split("\n")

wire_dict = {}
for line in wires:
    item = line.split(":")
    wire_dict[item[0]] = int(item[1])

for line in wires_two:
    split_item = line.split("->")
    #print(split_item)
    split_again = re.split(r"\s+AND\s+|\s+OR\s+|\s+XOR\s+",split_item[0])
    if split_again[0] not in wire_dict:
        wire_dict[split_again[0]] = -1
    if split_again[1] not in wire_dict:
        wire_dict[split_again[1]] = -1
    if split_item[1] not in wire_dict:
        wire_dict[split_item[1].replace(" ","")] = -1
    # if 'OR' in split_item[0]:
    #     pass
    # if 'AND' in split_item[0]:
    #     pass
    # if 'XOR' in split_item[0]:
    #     pass

def check_if_z_undefined(strings):
    for wire in strings:
        if wire[0] == 'z' and strings[wire] == -1:
            return False

    return True

def calc_wires(wires_dict, wire_info):
    counter = 0

    while ((check_if_z_undefined(wires_dict)) == False):
        counter +=1
        for wires in wire_info:
            #print(wires_dict)
            if check_if_z_undefined(wires_dict) == True:
                return wires_dict
            split_item = wires.split("->")
        #print(split_item)
            split_again = re.split(r"\s+AND\s+|\s+OR\s+|\s+XOR\s+",split_item[0])
            w3 = split_item[1].replace(" ","")
            w2 = split_again[1].replace(" ","")
            w1 = split_again[0].replace(" ","")
            #print(f"w1 is {wires_dict[w1]} w2 is {wires_dict[w2]} and w3 is {w3}")
            if wires_dict[w2] == -1 or wires_dict[w1] == -1:
                continue
            if 'XOR' in split_item[0]:
                wires_dict[w3] = wires_dict[w1] ^ wires_dict[w2]
                continue
            if 'OR' in split_item[0]:
                wires_dict[w3] = wires_dict[w1] | wires_dict[w2]
                continue
            if 'AND' in split_item[0]:
                wires_dict[w3] = wires_dict[w1] & wires_dict[w2]
                continue

    return wires_dict

answ = calc_wires(wire_dict, wires_two)
#print(calc_wires(wire_dict, wires_two))
#print(wire_dict)
final_answ = 0
counter = 0
for item in sorted(answ):
    if item[0] == 'z':
        print(f"The value of wire {item} is {wire_dict[item]}")
        final_answ += wire_dict[item] << counter
        counter += 1
print(bin(final_answ))
print(final_answ)
