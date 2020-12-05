import math

class BoardingPass:
    def __init__(self, seatcode):
        rowcode = seatcode[:7]
        columncode = seatcode[7:]
        self.row = self.parseCode(rowcode)
        self.column = self.parseCode(columncode)
        self.seat_id = self.row * 8 + self.column

    def parseCode(self, code):
        _max = 2 ** len(code) - 1
        _min = 0

        for cmd in code:
            _mid = (_min + _max) / 2

            if cmd == 'F' or cmd == 'L':
                _max = math.floor(_mid)
            elif cmd == 'B' or cmd == 'R':
                _min = math.ceil(_mid)

        return _min

def bySeatId(boardingpass):
    return boardingpass.seat_id

f = open("day5.txt")

boardingpasses = []
highest_seat_id = -1

for line in f:
    boardingpasses.append(BoardingPass(line[:-1]))
    if boardingpasses[-1].seat_id > highest_seat_id:
        highest_seat_id = boardingpasses[-1].seat_id

my_seat = -1
boardingpasses.sort(key=bySeatId)
for x in range(len(boardingpasses) - 1):
    seat_id_diff = boardingpasses[x + 1].seat_id - boardingpasses[x].seat_id
    if  seat_id_diff > 1:
        my_seat = boardingpasses[x].seat_id + 1
        break

print("Part 1: The highest seatID is %d" % highest_seat_id)
print("Part 2: My seatID is %d" % my_seat)
