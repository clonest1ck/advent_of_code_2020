
def part_1(expenses):
    i = 0
    while i < len(expenses):
        first = expenses[i]
        j = len(expenses) - 1
        while j > i and first + expenses[j] > 2020:
            j -= 1
        if first + expenses[j] == 2020:
            return first * expenses[j]
        i += 1
    return -1

def part_2(expenses):
    i = 0
    while i < len(expenses):
        first = expenses[i]
        j = len(expenses) - 2
        while j > i:
            second = expenses[j]
            k = len(expenses) - 1
            while k > j:
                third = expenses[k]
                if first + second + third == 2020:
                    return first * second * third
                k -= 1
            j -= 1
        i += 1
    return -1


f = open('day1.txt')

expenses = []

for line in f:
    expenses.append(int(line))

expenses.sort()

result = part_1(expenses)
print("Part 1: Product %d" % result)

result = part_2(expenses)
print("Part 2: Product %d" % result)
