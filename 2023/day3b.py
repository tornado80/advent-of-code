from typing import List

with open("input-day3.txt", "r") as f:
    lines = f.readlines()

row_count = len(lines)
column_count = len(lines[0]) - 1
map: List[str] = []
top_row = "".join(["." for _ in range(column_count + 2)])
map.append(top_row)
for line in lines:
    map.append("." + line[:-1] + ".")
map.append(top_row)

stars = {}

def any_symbol_around_me(row_index, begin_index, end_index, number):
    for i in range(row_index - 1, row_index + 2):
        for j in range(begin_index - 1, end_index + 2):
            c = map[i][j]
            if c == "*":
                if (i, j) not in stars:
                    stars[(i, j)] = [number]
                else:
                    stars[(i, j)].append(number)
                return True
            if c != "." and not c.isdigit():
                return True
    return False

number = None
begin_index = 0
end_index = 0
result1 = 0
for i in range(row_count):
    print("line", i + 1, ":", end=" ")
    for j in range(column_count):
        c = map[i + 1][j + 1]
        if c.isdigit():
            if number is None:
                number = int(c)
                begin_index = j
            else:
                number = number * 10 + int(c)
            if not map[i + 1][j + 2].isdigit():
                end_index = j
                if any_symbol_around_me(i + 1, begin_index + 1, end_index + 1, number):
                    print(number, end=", ")
                    result1 += number
                number = None
    print()

result2 = 0

for key, value in stars.items():
    print(key, value)
    if len(value) == 2:
        result2 += value[0] * value[1]

print(result2)