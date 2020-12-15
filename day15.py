def step(counter, previous, history):
    occurs = history[previous]
    new = 0

    if len(occurs) > 1:
        new = occurs[-1] - occurs[-2]

    if new not in history:
        history[new] = []

    history[new].append(counter)

    if len(history[number]) > 2:
        history[number] = history[number][-2:]

    previous = new
    counter += 1

    return counter, previous

f = open("day15.txt")

starting = [int(x) for x in f.readline().split(",")]

f.close()

counter = 1
previous = 0
history = {}

for number in starting:
    if number not in history:
        history[number] = []
    history[number].append(counter)
    previous = number
    counter += 1

while counter <= 2020:
    counter, previous = step(counter, previous, history)

print("Part 1: The 2020th number is %d" % previous)

while counter <= 30000000:
    counter, previous = step(counter, previous, history)

print("Part 2: The 30000000th number is %d" % previous)
