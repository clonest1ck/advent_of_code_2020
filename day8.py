from enum import Enum

class Command(Enum):
    ACC = 1
    JMP = 2
    NOP = 3

    def fromString(cmd_string):
        if "acc" == cmd_string:
            return Command.ACC
        elif "jmp" == cmd_string:
            return Command.JMP
        elif "nop" == cmd_string:
            return Command.NOP
        else:
            raise "Not a valid command %s" % cmd_string

class Operation:
    def __init__(self, cmd, arg):
        self.command = cmd
        self.arg = arg

def run(memory):
    visited = {}
    memsize = len(memory)
    pc = 0
    ac = 0

    while True:
        if pc in visited or pc >= memsize:
            break

        visited[pc] = 1
        op = memory[pc]

        if op.command == Command.ACC:
            ac += op.arg
        elif op.command == Command.NOP:
            ac = ac
        elif op.command == Command.JMP:
            pc += op.arg
            continue
        pc += 1

    return pc, ac

def changeOperation(op):
    arg = op.arg
    cmd = op.command
    if op.command == Command.JMP:
        cmd = Command.NOP
    elif op.command == Command.NOP and op.arg != 0:
        cmd = Command.JMP
    return Operation(cmd, arg)


f = open("day8.txt")
memory = []

for line in f:
    cmd_s, arg_s = line.split(' ')
    cmd = Command.fromString(cmd_s)
    arg = int(arg_s)

    memory.append(Operation(cmd, arg))

pc, ac_1 = run(memory)

mc = -1
while pc != len(memory):
    if mc != -1:
        # restore changed cmd
        op = memory[mc]
        op = changeOperation(op)
        memory[mc] = op
    mc += 1
    op = memory[mc]
    op = changeOperation(op)
    if op.command == memory[mc].command:
        continue
    memory[mc] = op
    pc, ac_2 = run(memory)

print("Part 1: ac = %d" % ac_1)
print("Part 2: ac = %d" % ac_2)

