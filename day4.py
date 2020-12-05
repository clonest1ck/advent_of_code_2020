class Passport:
    def __init__(self, data):
        self.data = {}
        self.required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

        for field, value in data.items():
            self.data[field] = value

        self.has_all_fields = True
        for required in self.required_fields:
            if not required in self.data:
                self.has_all_fields = False
                break

        self.is_valid = self.has_all_fields
        for field, value in self.data.items():
            if not self.is_valid:
                break
            if field == "byr" and not self.valueIsBetween(value, 1920, 2002):
                self.is_valid = False
            elif field == "iyr" and not self.valueIsBetween(value, 2010, 2020):
                self.is_valid = False
            elif field == "eyr" and not self.valueIsBetween(value, 2020, 2030):
                self.is_valid = False
            elif field == "hgt":
                height = value[:-2]
                unit = value[-2:]
                _min = 0
                _max = 0
                if unit == "cm":
                    _min = 150
                    _max = 193
                elif unit == "in":
                    _min = 59
                    _max = 76
                if not self.valueIsBetween(height, _min, _max):
                    self.is_valid = False
            elif field == "hcl":
                prefix = value[0]
                length = len(value)
                intval = 0
                try:
                    intval = int(value[1:], 16)
                except:
                    intval = -1
                if not (prefix == '#' and length == 7 and self.valueIsBetween(intval, 0, int("ffffff", 16))):
                    self.is_valid = False
            elif field == "ecl":
                valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if value not in valid_colors:
                    self.is_valid = False
            elif field == "pid":
                length = len(value)
                intval = 0
                try:
                    intval = int(value, 10)
                except:
                    intval = -1
                if not (length == 9 and self.valueIsBetween(intval, 0, 999999999)):
                    self.is_valid = False

    def valueIsBetween(self, value, _min, _max):
        intval = _min - 1
        try:
            intval = int(value)
        except:
            intval = _min -1

        return (_min <= intval and intval <= _max)

f = open('day4.txt')

passports = []

fields = {}
for line in f:
    line = line[:-1] # remove newline
    if len(line) == 0:
        passports.append(Passport(fields))
        fields = {}
    else:
        for field in line.split(" "):
            key, value = field.split(":")
            fields[key] = value

passports.append(Passport(fields))

has_all_fields = 0
for passport in passports:
    if passport.has_all_fields:
        has_all_fields += 1

is_valid = 0
for passport in passports:
    if passport.is_valid:
        is_valid += 1

print("Part 1: There are %d passports with all required fields" % has_all_fields)
print("Part 2: There are %d valid passports" % is_valid)
