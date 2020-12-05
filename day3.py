
class Tile:
    def __init__(self, is_tree):
        self.is_tree = is_tree


def Travel(tiles, dx, dy):
    mapwidth = len(tiles[0]) - 1
    mapheight = len(tiles)
    x = dx % mapwidth
    y = dy
    trees = 0

    while y < mapheight:
        is_tree = tiles[y][x].is_tree
        if tiles[y][x].is_tree:
            trees += 1
        x = (x + dx) % mapwidth
        y += dy

    return trees


f = open('day3.txt')

tiles = []

for line in f:
    row = []
    for tile in line:
        if tile == "#":
            row.append(Tile(True))
        else:
            row.append(Tile(False))
    tiles.append(row)

trees = Travel(tiles, 3, 1)
print("Part 1: We encountered %d trees" % trees)

trees_1 = Travel(tiles, 1, 1)
trees_2 = trees
trees_3 = Travel(tiles, 5, 1)
trees_4 = Travel(tiles, 7, 1)
trees_5 = Travel(tiles, 1, 2)
product = trees_1 * trees_2 * trees_3 * trees_4 * trees_5
print("Part 2: The product is %d" % product)

