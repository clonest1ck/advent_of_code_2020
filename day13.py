
def isInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def getSecond(bus):
    return bus[1]

def getFirst(bus):
    return bus[0]

f = open("day13.txt")
data = f.readlines()
f.close()

earliest = int(data[0])
busses = [(int(number), int(number) - (earliest % int(number))) for number in data[1].split(",") if isInt(number)]
busses.sort(key=getSecond)

print("Part 1: %d" % (busses[0][0] * busses[0][1]))

f = open("day13.txt")
data = f.readlines()
f.close()
busses = data[1][:-1].split(",")
num_busses = len(busses)

busses = [(int(busses[i]), i) for i in range(num_busses) if isInt(busses[i])]
first = busses[0][0]

busses.sort(key=getFirst, reverse=True)
frequency = busses[0][0]
index = busses[0][1]

busses = [(bus[0], bus[1] - index) for bus in busses]

needle = 1
zeropoint = 0

while needle < len(busses):
    zeropoint += frequency
    if ((zeropoint + busses[needle][1]) % busses[needle][0]) == 0:
        frequency = frequency * busses[needle][0]
        needle += 1

for bus, index in busses:
    if bus == first:
        zeropoint += index
        break

print("Part 2: %d" % zeropoint)
