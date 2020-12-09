
def isSumOfLastInterval(current, interval):
    _min = 0
    _max = len(interval) - 1

    while _min < _max:
        _sum = interval[_min] + interval[_max]
        if current == _sum:
            return True
        elif current > _sum:
            _min += 1
        elif current < _sum:
            _max -= 1

    return False

def insertToInterval(current, interval):
    index = 0
    interval_len = len(interval)
    while index < interval_len and current > interval[index]:
        index += 1

    interval.insert(index, current)


f = open("day9.txt")

numbers = {}
last_interval = []
base = 0
interval = 25

for line in f:
    current = int(line)
    numbers[base] = current

    if base >= interval:
        valid = isSumOfLastInterval(current, last_interval)
        if not valid:
            break

        to_replace = numbers[base - interval]
        index = last_interval.index(to_replace)
        last_interval = last_interval[:index] + last_interval[index+1:]
    base += 1
    insertToInterval(current, last_interval)

magic_number = numbers[base]

data = []
for i in range(base):
    data.append(numbers[i])

start = 0
end = 1

while start < base - 1:
    end = start + 1
    while sum(data[start:end + 1]) < magic_number:
        end += 1

    if sum(data[start:end + 1]) == magic_number:
        break

    start += 1

magic_sum = min(data[start:end + 1]) + max(data[start:end + 1])

print("Part 1: %d is not a sum of any pair of the last %d numbers" % (magic_number, interval))
print("Part 2: %d is the magic number" % (magic_sum))
