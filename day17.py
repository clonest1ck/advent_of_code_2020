def update(cubes, is_4d = False):
    new_state = {}
    adjacent_active = {}

    _range = [-1, 0, 1]
    w_range = _range
    if not is_4d:
        w_range = [0]

    for x, y, z, w in cubes.keys():
        for dx in _range:
            for dy in _range:
                for dz in _range:
                    for dw in w_range:

                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        coord = (x + dx, y + dy, z + dz, w + dw)
                        if not coord in adjacent_active:
                            adjacent_active[coord] = 0
                        adjacent_active[coord] += 1

    for cube in adjacent_active.keys():
        if cube in cubes:
            active_neighbours = adjacent_active[cube]
            if active_neighbours == 2 or active_neighbours == 3:
                new_state[cube] = True
        else:
            active_neighbours = adjacent_active[cube]
            if active_neighbours == 3:
                new_state[cube] = True

    return new_state

f = open("day17.txt")

z = 0
w = 0
y = 0

cubes = {}

for line in f:
    x = 0
    for cube in line:
        if cube == "#":
            cubes[(x, y, z, w)] = True
        x += 1
    y += 1

state = cubes

for cycle in range(6):
    state = update(state)

print("Part 1: There are %d active cubes" % len(state.keys()))

state = cubes
for cycle in range(6):
    state = update(state, True)

print("Part 2: There are %d active cubes" % len(state.keys()))
