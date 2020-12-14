
def parseMaskV1(argument):
    mask = {}
    argument = argument[::-1]

    for power in range(len(argument)):
        if argument[power] != 'X':
            mask[power] = argument[power]

    return mask

def applyMaskV1(mask, value):
    binary_str_reversed = list(format(value, "036b")[::-1])

    for power in range(len(binary_str_reversed)):
        if power in mask:
            binary_str_reversed[power] = mask[power]

    binary_str = binary_str_reversed[::-1]
    return int("".join(binary_str), 2)

def extractValues(index, values):
    if index >= len(values):
        return []

    result = []
    for value in values[index]:
        next_result = extractValues(index + 1, values)
        if len(next_result) == 0:
            result.append([value])
        else:
            for res in next_result:
                result.append([value] + res)

    return result

def applyMaskV2(mask, value):
    values = []
    binary_str = format(value, "036b")

    for bit in range(len(mask)):
        bitmask = []
        if mask[bit] == "X":
            bitmask = ['0', '1']
        elif mask[bit] == "0":
            bitmask = [binary_str[bit]]
        elif mask[bit] == "1":
            bitmask = ["1"]
        values.append(bitmask)

    return list(map("".join, extractValues(0, values)))


f = open("day14.txt")

mask = {}
memory = {}

for line in f:
    line = line[:-1] # remove newline
    command, argument = line.split(" = ")
    if command == "mask":
        mask = parseMaskV1(argument)
    else:
        address = int(command[command.index('[') + 1:command.index(']')])
        argument = int(argument)
        argument = applyMaskV1(mask, argument)
        memory[address] = argument

f.close()
print("Part 1: The sum of the address space is %d" % sum(memory.values()))

f = open("day14.txt")

mask = ""
memory = {}

for line in f:
    line = line[:-1] # remove newline
    command, argument = line.split(" = ")
    if command == "mask":
        mask = argument
    else:
        address = int(command[command.index('[') + 1:command.index(']')])
        argument = int(argument)
        addresses = applyMaskV2(mask, address)
        for address in addresses:
            memory[address] = argument

f.close()
print("Part 2: The sum of the address space is %d" % sum(memory.values()))
