
class Bag:
    def __init__(self, color, contains):
        self.color = color
        self.contains = contains


def containsAnyOf(rules, color, needle):
    if needle in rules[color].contains.keys():
        return True
    for _color in rules[color].contains.keys():
        if containsAnyOf(rules, _color, needle):
            return True

    return False

def getBagsInside(bag, rules, bags_inside):
    total = 0
    for inside, amount in bag.contains.items():
        if not inside in bags_inside:
            bags_inside[inside] = getBagsInside(rules[inside], rules, bags_inside)
        total += amount * (1 + bags_inside[inside])
    return total

def getContainLen(value):
    return len(value.contains)

f = open('day7.txt')

rules = {}

for line in f:
    contains = {}
    color, contains_str = line.split("bags contain")
    color = color.strip()
    for bagtype in contains_str.split(','):
        amount = 0
        amount_value = bagtype.split(' ')[1].strip()
        if amount_value != "no":
            amount = int(bagtype.split(' ')[1])
            bagcolor = bagtype.split(" bag")[0][bagtype.index(' ', 1) + 1:].strip()
            contains[bagcolor] = amount
    rules[color] = Bag(color, contains)

bags_with_a_shiny_gold_bag = 0
needle = "shiny gold"
for color, bags in rules.items():
    if color != needle:
        if containsAnyOf(rules, color, needle):
            bags_with_a_shiny_gold_bag += 1

bags_inside = {}
sorted_rules = list(rules.values())
sorted_rules.sort(key=getContainLen)
for bag in sorted_rules:
    if not bag.color in bags_inside:
        bags_inside[bag.color] = getBagsInside(bag, rules, bags_inside)

print("Part 1: There are %d bags which contain at least one %s" % (bags_with_a_shiny_gold_bag, needle))
print("Part 2: We need to have %d bags in our %s bag" % (bags_inside[needle], needle))
