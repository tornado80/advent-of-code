with open("2023/input-day11.txt") as f:
    lines = f.readlines()

row_count = len(lines)
column_count = len(lines[0]) - 1
galaxies = []
rows = [0 for _ in range(row_count)]
columns = [0 for _ in range(column_count)]

for i, line in enumerate(lines):
    for j, c in enumerate(line.strip()):
        if c == "#":
            galaxies.append((i, j))
            rows[i] = 1
            columns[j] = 1

for i in range(row_count):
    if rows[i] == 0:
        rows[i] = 1000000

for i in range(column_count):
    if columns[i] == 0:
        columns[i] = 1000000

s = 0

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        s += sum(rows[min(x1, x2):max(x1, x2)]) + sum(columns[min(y1, y2):max(y1, y2)])

print(s)

            


