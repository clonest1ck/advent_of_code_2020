import math

class Tile:
    def __init__(self, _id, data):
        self.id = _id
        self.data = data
        self.update()
        self.right = None
        self.below = None
        self.rotation = 0
        self.flipped = 0

    def update(self):
        self.top = "".join(self.data[0])
        self.bottom = "".join(self.data[-1])
        self.left = "".join([d[0] for d in self.data])
        self.right = "".join([d[-1] for d in self.data])

        self.t_val = int(self.top, 2)
        self.b_val = int(self.bottom, 2)
        self.l_val = int(self.left, 2)
        self.r_val = int(self.right, 2)

    def reset(self):
        while self.rotation > 0:
            self.rotate()
        while self.flipped > 0:
            self.flip()
        self.right = None
        self.below = None

    # Rotate 90 deg clockwise
    def rotate(self):
        data = []
        for i in range(len(self.data)):
            new_row = []
            for row in self.data:
                new_row.append(row[i])
            new_row.reverse()
            data.append(new_row)
        self.rotation = (self.rotation + 1) % 4
        self.data = data
        self.update()

    #flip x-axis
    def flip(self):
        self.data.reverse()
        self.flipped = (self.flipped + 1) % 2

class Image:
    def __init__(self, max_x, max_y, tiles):
        data = []
        for y in range(max_y):
            section = []
            tilerow = [tiles[(x, y)] for x in range(max_x)]
            for _y in range(1, len(tilerow[0].data) - 1):
                row = []
                for tile in tilerow:
                    row += tile.data[_y][1:-1]
                section.append(row)
            data += section
        self.data = data

    # Rotate 90 deg clockwise
    def rotate(self):
        data = []
        for i in range(len(self.data)):
            new_row = []
            for row in self.data:
                new_row.append(row[i])
            new_row.reverse()
            data.append(new_row)
        self.data = data

    #flip x-axis
    def flip(self):
        self.data.reverse()

    def hasSeamonsterAt(self, x, y):
        seamonster = [ "                  # "
                     , "#    ##    ##    ###"
                     , " #  #  #  #  #  #   "
                     ]

        are_monster = set()
        for dy in range(len(seamonster)):
            if y + dy >= len(self.data):
                return set()
            for dx in range(len(seamonster[0])):
                if x + dx >= len(self.data[0]):
                    return set()

                if seamonster[dy][dx] == "#":
                    if self.data[y+dy][x+dx] != "1":
                        return set()
                    else:
                        are_monster.add((x+dx, y+dy))
        return are_monster

    def findSeamonsters(self):
        monsters = 0
        are_monsters = set()
        y = 0
        while y < len(self.data):
            x = 0
            while x < len(self.data[0]):
                are_monster = self.hasSeamonsterAt(x, y)
                if len(are_monster) > 0:
                    monsters += 1
                    are_monsters.update(are_monster)
                x += 1
            y += 1

        return (monsters, len(are_monsters))


class TileState:
    def __init__(self, tile_id, top, bottom, left, right, rotation, flip):
        self.id = tile_id
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.rotation = rotation
        self.flip = flip

    def __eq__(self, other):
        return self.id == other.id and \
               self.top == other.top and \
               self.bottom == other.bottom and \
               self.left == other.left and \
               self.right == other.right

def toBinary(c):
    if c == ".":
        return "0"
    elif c == "#":
        return "1"
    return ""

f = open("day20.txt")

new_tile = True
tiles = {}
states = []
current_tile = []
tile_id = -1
for line in f:
    if new_tile:
        tile_id = int(line.split(" ")[1].split(":")[0])
        new_tile = False
    elif line == "\n":
        tile = Tile(tile_id, current_tile)
        tiles[tile_id] = tile
        for flip in range(2):
            for rotation in range(4):
                already_added = False
                new_state = TileState(tile_id, tile.t_val, tile.b_val, tile.l_val, tile.r_val, rotation, flip)
                for state in states:
                    if state == new_state:
                        already_added = True
                        break
                if not already_added:
                    states.append(new_state)
                tile.rotate()
            tile.flip()
        tile.reset()
        new_tile = True
        current_tile = []
    else:
        line = "".join(map(toBinary, line))
        current_tile.append(line)

used_ids = set()
max_x = int(math.sqrt(len(tiles)))
max_y = max_x

def tryPosition(x, y, state, states_left):
    solutions = []
    for i in range(len(states_left)):
        new = states_left[i]
        valid = True
        _x = x - 1
        _y = y - 1
        if not _x < 0:
            valid = valid and state[(_x, y)].right == new.left
        if not _y < 0:
            valid = valid and state[(x, _y)].bottom == new.top
        for coord, tile in state.items():
            valid = valid and (tile.id != new.id)

        if valid:
            _x = x + 1
            _y = y
            if _x == max_x:
                _y = _y + 1
                _x = 0

            new_state = {s:state[s] for s in state.keys()}
            new_state[(x, y)] = new
            if _y == max_y and valid:
                return new_state

            new_left = [a for a in states_left if not a == new]
            result = tryPosition(_x, _y, new_state, new_left)
            if len(result.keys()) != 0:
                return result
                solutions.append((len(result.keys()), result))
    best = (0, {})
    for solution in solutions:
        if solution[0] > best[0]:
            best = solution
    return best[1]

result = tryPosition(0, 0, {}, states)

product = result[(0,0)].id * result[(0,max_y-1)].id * result[(max_x-1,0)].id * result[(max_x-1,max_y-1)].id

print("Part 1: The product is %d" % product)

img = {}
for coord, state in result.items():
    tile = tiles[state.id]
    for flip in range(state.flip):
        tile.flip()
    for rotation in range(state.rotation):
        tile.rotate()
    img[coord] = tile

image = Image(max_x, max_y, img)

checked = []
for flip in range(2):
    for rotation in range(4):
        checked.append(image.findSeamonsters())
        image.rotate()
    image.flip()

most = 0
covered_tiles = 0
for monsters, marked in checked:
    if monsters > most:
        most = monsters
        covered_tiles = marked

rough_tiles = 0
for row in image.data:
    for pixel in row:
        if pixel == "1":
            rough_tiles += 1

print("Part 2: Water roughnesss is %d" % (rough_tiles - covered_tiles))
