from enum import IntEnum
import math

def sign(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    return 0

class Direction(IntEnum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

    def fromString(s):
        if s == "N":
            return Direction.NORTH
        elif s == "E":
            return Direction.EAST
        elif s == "S":
            return Direction.SOUTH
        elif s == "W":
            return Direction.WEST

class Boat:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.direction = d

    def turn(self, way, deg):
        amount = deg / 90
        if way == "L":
            self.direction = Direction((int(self.direction) - amount) % 4)
        elif way == "R":
            self.direction = Direction((int(self.direction) + amount) % 4)

    def move(self, direction, amount):
        if direction == "F":
            direction = self.direction
        else:
            direction = Direction.fromString(direction)

        if direction == Direction.EAST:
            self.x += amount
        elif direction == Direction.SOUTH:
            self.y -= amount
        elif direction == Direction.WEST:
            self.x -= amount
        elif direction == Direction.NORTH:
            self.y += amount

class Waypoint:
    def __init__(self, boat):
        self.x = 10
        self.y = 1
        self.boat = boat

    def turn(self, way, deg):
        angle = math.radians(deg)
        if way == "R":
            angle = -angle

        dx = self.x * math.cos(angle) - self.y * math.sin(angle)
        dy = self.y * math.cos(angle) + self.x * math.sin(angle)

        self.x = dx
        self.y = dy

    def move(self, direction, amount):
        if direction == "F":
            dx = self.x * amount
            dy = self.y * amount
            self.boat.x += dx
            self.boat.y += dy
            return

        direction = Direction.fromString(direction)

        if direction == Direction.EAST:
            self.x += amount
        elif direction == Direction.SOUTH:
            self.y -= amount
        elif direction == Direction.WEST:
            self.x -= amount
        elif direction == Direction.NORTH:
            self.y += amount

f = open("day12.txt")

instructions = []

for line in f:
    instructions.append((line[0], int(line[1:])))

boat = Boat(0, 0, Direction.EAST)

for action, amount in instructions:
    if action == "L" or action == "R":
        boat.turn(action, amount)
    else:
        boat.move(action, amount)

print("Part 1: Manhattan distance to location is %d units" % (abs(boat.x) + abs(boat.y)))

boat = Boat(0, 0, Direction.EAST)
waypoint = Waypoint(boat)

for action, amount in instructions:
    if action == "L" or action == "R":
        waypoint.turn(action, amount)
    else:
        waypoint.move(action, amount)

print("Part 2: Manhattan distance to location is %d units" % (abs(boat.x) + abs(boat.y)))

