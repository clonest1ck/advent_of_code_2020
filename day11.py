
class Tile:
    def __init__(self, is_seat, is_occupied):
        self.is_seat = is_seat
        self.is_occupied = is_occupied

    def __str__(self):
        if not self.is_seat:
            return "."
        if not self.is_occupied:
            return "L"
        return "#"

def doRound(waiting_area, max_occupied, depth):
    directions = [(y, x) for y in range(-1, 2) for x in range(-1, 2) if not (x == 0 and y == 0)]
    new_waiting_area = []
    changed = 0
    occupied = 0

    min_y = 0
    max_y = len(waiting_area) - 1

    for y in range(max_y + 1):
        row = []
        min_x = 0
        max_x = len(waiting_area[y]) - 1
        for x in range(max_x + 1):
            row.append(waiting_area[y][x])
            if not waiting_area[y][x].is_seat:
                continue
            occupied_neighbours = 0
            for dy, dx in directions:
                first_match = None
                step = 1
                while first_match == None and step <= depth:
                    _y = y + dy * step
                    _x = x + dx * step
                    step += 1
                    if _y < min_y or _y > max_y or _x < min_x or _x > max_x:
                        break

                    tile = waiting_area[_y][_x]
                    if not tile.is_seat:
                        continue

                    first_match = tile
                    break

                if first_match != None and first_match.is_occupied:
                    occupied_neighbours += 1


            if occupied_neighbours == 0:
                row[-1] = Tile(True, True)
            elif occupied_neighbours >= max_occupied:
                row[-1] = Tile(True, False)

            if row[-1].is_occupied != waiting_area[y][x].is_occupied:
                changed += 1

            if row[-1].is_occupied:
                occupied += 1

        new_waiting_area.append(row)

    return changed, occupied, new_waiting_area

f = open("day11.txt")

waiting_area = []

for line in f:
    row = []
    for tile in line:
        is_seat = tile == "L" or tile == "#"
        is_occupied = tile == "#"
        row.append(Tile(is_seat, is_occupied))

    waiting_area.append(row)

changed = 1
occupied = 0
area_1 = waiting_area

while changed > 0:
    changed, occupied, area_1 = doRound(area_1, 4, 1)

print("Part 1: There are %d seats occupied when no more changes can be made" % occupied)

changed = 1
occupied = 0
area_2 = waiting_area

while changed > 0:
    changed, occupied, area_2 = doRound(area_2, 5, 2 * len(area_2))

print("Part 2: There are %d seats occupied when no more changes can be made" % occupied)
