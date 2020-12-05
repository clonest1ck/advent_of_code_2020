
class Password:
    def __init__(self, pswd, char, _min, _max):
        self.pswd = pswd
        self.char = char
        self.min = _min
        self.max = _max



def part_1(passwords):
    valid = 0
    for password in passwords:
        counts = password.pswd.count(password.char)
        if counts >= password.min and counts <= password.max:
            valid += 1

    return valid

def part_2(passwords):
    valid = 0
    for password in passwords:
        _first = password.pswd[password.min - 1]
        _second = password.pswd[password.max - 1]
        char = password.char
        if (_first == char and _second != char) or (_first != char and _second == char):
            valid += 1

    return valid


f = open('day2.txt')

passwords = []

for line in f:
    minmax, ch, pswd = line.split(' ')
    _min = int(minmax.split('-')[0])
    _max = int(minmax.split('-')[1])
    char = ch[0]
    passwords.append(Password(pswd, char, _min, _max))

valid = part_1(passwords)
print("Part 1: There are %d valid passwords" % valid)

valid = part_2(passwords)
print("Part 2: There are %d valid passwords" % valid)
