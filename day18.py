class Number:
    def __init__(self, lhs):
        self.lhs = int(lhs)

    def evaluate(self):
        return self

class Parenthesis:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        return self.expression.evaluate()

class Operator:
    def __init__(self, operator):
        self.operator = operator

    def evaluate(self, lhs, rhs):
        if self.operator == "*":
            return Number(lhs.evaluate().lhs * rhs.evaluate().lhs)
        elif self.operator == "+":
            return Number(lhs.evaluate().lhs + rhs.evaluate().lhs)
        else:
            raise ValueError

class Expression:
    def __init__(self, lhs, operator, rhs):
        self.lhs = lhs
        self.operator = operator
        self.rhs = rhs

    def evaluate(self):
        if type(self.rhs) == Expression:
            self.rhs.lhs = self.operator.evaluate(self.lhs, self.rhs.lhs)
            return self.rhs.evaluate()
        else:
            return self.operator.evaluate(self.lhs, self.rhs)

def findEndOfParenthesis(line):
    inside = 0
    next_start = line.index("(")
    next_end = line.index(")")

    while True:
        smallest = next_end
        if next_start < next_end:
            inside += 1
            smallest = next_start
        elif inside > 0:
            inside -= 1

        if inside == 0:
            break

        try:
            next_start = line.index("(", smallest + 1)
        except:
            next_start = len(line)

        try:
            next_end = line.index(")", smallest + 1)
        except:
            next_end = len(line)

    return next_end

def parseExpression(line, evaluate_addition = False):
    lhs = Number(0)
    rhs = Number(0)
    operator = Operator("+")
    start = 0
    end = 0

    line = line.strip()
    line = line + " "

    if line[0] == "(":
        end = findEndOfParenthesis(line)
        start = 1
        lhs = Parenthesis(parseExpression(line[start:end], evaluate_addition)).evaluate()
    else:
        end = line.index(" ")
        try:
            if line.index(")") < end:
                end = line.index(")")
        except:
            end = end

        lhs = Number(line[start:end])
        end = line.index(" ")

    try:
        start_mul = line.index("*", end)
    except:
        start_mul = len(line)
    try:
        start_add = line.index("+", end)
    except:
        start_add = len(line)

    start = min(start_mul, start_add)

    is_addition = start == start_add

    end = start + 1

    if len(line) == start:
        return lhs

    operator = Operator(line[start:end])
    line = line[end:]

    rhs = parseExpression(line, evaluate_addition)

    if is_addition and evaluate_addition:
        if type(rhs) == Expression:
            rhs.lhs = Number(lhs.lhs + rhs.lhs.lhs)
            return rhs
        else:
            lhs = Number(lhs.lhs + rhs.lhs)
            return lhs

    return Expression(lhs, operator, rhs)


f = open("day18.txt")
expressions = []

for line in f:
    expressions.append(parseExpression(line))

f.close()

total = 0
for expression in expressions:
    total += expression.evaluate().lhs

print("Part 1: the sum is %d" % total)

f = open("day18.txt")
expressions = []

for line in f:
    expressions.append(parseExpression(line, True))

f.close()

total = 0
for expression in expressions:
    total += expression.evaluate().lhs

print("Part 2: the sum is %d" % total)
