file = open("computer.txt", "r")
data = file.read().split("\n")
REGISTER_A = 0
REGISTER_B = 0
REGISTER_C = 0

PROGRAM_COUNTER = 0

OUTPUT_LIST = []

def calc_combo_operand(operand):
    global REGISTER_A
    global REGISTER_B
    global REGISTER_C
    if operand == 0 or operand == 1 or operand == 2 or operand == 3:
        return operand
    if operand == 4:
        return REGISTER_A
    if operand == 5:
        return REGISTER_B
    if operand == 6:
        return REGISTER_C
    if operand == 7:
        return 7
        print("INVALID combo operand!")
def load_data(data_to_parse):
    global REGISTER_A
    global REGISTER_C
    global REGISTER_B
    instruction_list = []
    REGISTER_A = int(data_to_parse[0].split(":")[1])
    REGISTER_B = int(data_to_parse[1].split(":")[1])
    REGISTER_C = int(data_to_parse[2].split(":")[1])
    instruction_set_string = [int(x) for x in data_to_parse[3].split(":")[1].replace(" ","").split(",")]
    return instruction_set_string

INSTRUCTIONS = load_data(data)

print(INSTRUCTIONS)

def adv(operand):
    global REGISTER_A
    global PROGRAM_COUNTER
    REGISTER_A = int((REGISTER_A) / (2 ** calc_combo_operand(operand)))
    PROGRAM_COUNTER += 2

def bxl(operand):
    global REGISTER_B
    global PROGRAM_COUNTER
    REGISTER_B = REGISTER_B ^ operand
    PROGRAM_COUNTER += 2

def bst(operand):
    global REGISTER_B
    global PROGRAM_COUNTER
    REGISTER_B = (calc_combo_operand(operand)) % 8
    PROGRAM_COUNTER += 2

def jnz(operand):
    global PROGRAM_COUNTER
    global REGISTER_B
    global REGISTER_A
    if REGISTER_A == 0:
        PROGRAM_COUNTER += 2
        return
    PROGRAM_COUNTER = operand

def bxc(operand):
    global PROGRAM_COUNTER
    global REGISTER_B
    global REGISTER_C
    REGISTER_B = REGISTER_B ^ REGISTER_C
    PROGRAM_COUNTER += 2

def out(operand):
    global PROGRAM_COUNTER
    global OUTPUT_LIST
    OUTPUT_LIST.append(calc_combo_operand(operand) % 8)
    PROGRAM_COUNTER += 2

def bdv(operand):
    global REGISTER_A
    global REGISTER_B
    global PROGRAM_COUNTER
    REGISTER_B = int((REGISTER_A) / (2 ** calc_combo_operand(operand)))
    PROGRAM_COUNTER += 2

def cdv(operand):
    global REGISTER_A
    global REGISTER_C
    global PROGRAM_COUNTER
    REGISTER_C = int((REGISTER_A) / (2 ** calc_combo_operand(operand)))
    PROGRAM_COUNTER += 2

counter = 0
while(PROGRAM_COUNTER < len(INSTRUCTIONS)):
    print(INSTRUCTIONS[PROGRAM_COUNTER])
    op_code = INSTRUCTIONS[PROGRAM_COUNTER]
    curr_operand = INSTRUCTIONS[PROGRAM_COUNTER+1]
    if op_code == 0:
        adv(curr_operand)
    if op_code == 1:
        bxl(curr_operand)
    if op_code == 2:
        bst(curr_operand)
    if op_code == 3:
        jnz(curr_operand)
    if op_code == 4:
        bxc(curr_operand)
    if op_code == 5:
        out(curr_operand)
    if op_code == 6:
        bdv(curr_operand)
    if op_code == 7:
        cdv(curr_operand)



answ_string = ""
for num in OUTPUT_LIST:
    answ_string += str(num)
    answ_string += ','

print(answ_string[0:len(answ_string) - 1])