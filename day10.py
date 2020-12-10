def part1(adapters):
    diff = {}

    for i in range(len(adapters) - 1):
        source = adapters[i]

        drain = adapters[i + 1]

        delta = drain - source
        if delta not in diff:
            diff[delta] = 0
        diff[delta] += 1

    return diff[1] * diff[3]


def part2(adapters):
    visits = {0 : 1}

    for i in range(len(adapters) - 1):
        j = i + 1
        adapter = adapters[i]
        multiplier = visits[adapter]
        while j < len(adapters) and adapters[j] - adapter <= 3:
            visiting = adapters[j]
            if visiting not in visits:
                visits[visiting] = 0

            visits[visiting] += multiplier
            j += 1

    return visits[adapters[-1]]

f = open('day10.txt')

adapters = [0]

for line in f:
    adapters.append(int(line))

adapters.sort()
adapters.append(adapters[-1] + 3)

prod = part1(adapters)
combinations = part2(adapters)

print("Part 1: product = %d" % prod)
print("Part 2: combinations = %d" % combinations)
