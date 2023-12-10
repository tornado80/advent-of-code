with open("2023/input-day10.txt") as f:
    graph = {}
    lines = f.readlines()
    n = len(lines)
    m = len(lines[0]) - 1
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            if c == "|":
                graph[(i, j)] = [(i - 1, j), (i + 1, j)]
            if c == "-":
                graph[(i, j)] = [(i, j - 1), (i, j + 1)]
            if c == "F":
                graph[(i, j)] = [(i + 1, j), (i, j + 1)]
            if c == "L":
                graph[(i, j)] = [(i - 1, j), (i, j + 1)]
            if c == "J":
                graph[(i, j)] = [(i - 1, j), (i, j - 1)]
            if c == "7":
                graph[(i, j)] = [(i + 1, j), (i, j - 1)]
            if c == ".":
                graph[(i, j)] = []
            if c == "S":
                start = (i, j)
                graph[(i, j)] = [(i - 1, j), (i + 1, j)] # like | by examining the input manually
count = 0
prev = None
cur = start
loop = [start]
while True:
    for neighbor in graph[cur]:
        if neighbor != prev:
            prev = cur
            cur = neighbor
            loop.append(cur)
            break
    count += 1
    if cur == start:
        break
print(count, loop)
    