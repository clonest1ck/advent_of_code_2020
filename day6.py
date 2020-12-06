def keysWithValueEqualTo(fields, _key):
    _sum = 0
    for key, value in fields.items():
        if key == _key:
            continue
        if value == fields[_key]:
            _sum += 1
    return _sum

def get_first(item):
    return item[0]

def get_second(item):
    return item[1]

f = open('day6.txt')

reports = []

fields = {}
for line in f:
    line = line[:-1] # remove newline
    if len(line) == 0:
        reports.append((len(fields.keys()) - 1, keysWithValueEqualTo(fields, 'total')))
        fields = {}
    else:
        if 'total' not in fields:
            fields['total'] = 0
        fields['total'] += 1
        for char in line:
            if char not in fields:
                fields[char] = 0
            fields[char] += 1

reports.append((len(fields.keys()) - 1, keysWithValueEqualTo(fields, 'total')))

total_1 = sum(map(get_first, reports))
total_2 = sum(map(get_second, reports))

print("Part 1: the total sum is %d" % total_1)
print("Part 2: the total sum is %d" % total_2)
