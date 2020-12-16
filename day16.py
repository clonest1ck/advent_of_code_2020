def parseField(line):
    field, criteria = line.split(": ")
    valid_numbers = []

    for _range in criteria.split(" or "):
        start, end = map(int, _range.split("-"))
        valid_numbers += list(range(start, end + 1))

    return field, valid_numbers

def parseTicket(line):
    field_values = list(map(int, line.split(",")))
    return field_values

f = open("day16.txt")

field_labels = []
fields = {}
my_ticket = []
tickets = []
valid_tickets = []
invalid_fields = []
done_parsing_fields = False
done_parsing_my_ticket = False

for line in f:
    if len(line) == 1:
        if not done_parsing_fields:
            done_parsing_fields = True
        elif not done_parsing_my_ticket:
            done_parsing_my_ticket = True

        continue
    try:
        line.index("your ticket")
        continue
    except ValueError:
        lineindex = 0

    try:
        line.index("nearby tickets")
        continue
    except ValueError:
        lineindex = 0

    if not done_parsing_fields:
        field, valid_numbers = parseField(line)
        field_labels.append(field)

        for number in valid_numbers:
            if number not in fields:
                fields[number] = []
            fields[number].append(field)
    elif not done_parsing_my_ticket:
        my_ticket = parseTicket(line)
    else:
        tickets.append(parseTicket(line))

for ticket in tickets:
    valid = True
    for field in ticket:
        if field not in fields:
            invalid_fields.append(field)
            valid = False

    if valid:
        valid_tickets.append(ticket)

print("Part 1: Ticket error rate is %d" % sum(invalid_fields))

ticket_length = len(valid_tickets[0])
fields_for_place = []

for i in range(ticket_length):
    valid_fields = set(fields[valid_tickets[0][i]])
    for ticket in valid_tickets:
        valid_in = set(fields[ticket[i]])
        valid_fields = valid_fields & valid_in

    fields_for_place.append((i, valid_fields))

def getLengthOfSecond(a):
    return len(a[1])

def getFirst(a):
    return a[0]

i = 0
while i < ticket_length:
    fields_for_place.sort(key=getLengthOfSecond)
    current = fields_for_place[i]
    if len(current[1]) == 1:
        to_be_removed = list(current[1])[0]

        for field in fields_for_place[i + 1:]:
            field[1].remove(to_be_removed)

    i += 1

fields_for_place.sort(key=getFirst)

total = 1
for index, _set in fields_for_place:
    field_name = list(_set)[0]
    try:
        if field_name.index("departure") == 0:
            total *= my_ticket[index]
        else:
            raise ValueError
    except ValueError:
        continue

print("Part 2: the product is %d" % total)

