import re


with open('../../input/day_3_data.txt', 'r') as file:
    data = file.read()

def sum_valid_multiplications(memory):
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    matches = re.findall(pattern, memory)
    total = sum(int(x) * int(y) for x, y in matches)
    return total

def sum_valid_multiplications_enabled(memory):
    mul = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    do = r"do\(\)"
    dont = r"don't\(\)"

    is_enabled = True
    total = 0

    tokens = re.split(r"(mul\(\s*\d+\s*,\s*\d+\s*\)|do\(\)|don't\(\))", memory)

    for token in tokens:
        if not token.strip():
            continue

        if re.match(do, token):
            is_enabled = True

        elif re.match(dont, token):
            is_enabled = False

        elif re.match(mul, token) and is_enabled:
            x, y = map(int, re.findall(r"\d+", token))
            total += x * y

    return total

result1 = sum_valid_multiplications(data)
result2 = sum_valid_multiplications_enabled(data)

print("Sum of results:", result1)
print("Sum of enabled results:", result2)