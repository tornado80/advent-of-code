with open("2023/input-day10.txt") as f:
    original_grid = []
    graph = {}
    lines = f.readlines()
    n = len(lines)
    m = len(lines[0]) - 1
    original_grid.append(["." for _ in range(m + 2)])
    for i, line in enumerate(lines):
        original_grid.append(["."])
        for j, c in enumerate(line.strip()):
            original_grid[-1].append(c)
            if c == "|":
                graph[(i, j)] = [(i - 1, j), (i + 1, j)]
            if c == "-":
                graph[(i, j)] = [(i, j + 1), (i, j - 1)]
            if c == "F":
                graph[(i, j)] = [(i, j + 1), (i + 1, j)]
            if c == "L":
                graph[(i, j)] = [(i - 1, j), (i, j + 1)]
            if c == "J":
                graph[(i, j)] = [(i, j - 1), (i - 1, j)]
            if c == "7":
                graph[(i, j)] = [(i, j - 1), (i + 1, j)]
            if c == ".":
                graph[(i, j)] = []
            if c == "S":
                start = (i, j)
        original_grid[-1].append(".")
    original_grid.append(["." for _ in range(m + 2)])

a = start[0] + 1
b = start[1] + 1

if original_grid[a - 1][b] == "|" and original_grid[a + 1][b] == "|": # |
    graph[start] = [(start[0] - 1, start[1]), (start[0] + 1, start[1])]
    print("|")

if original_grid[a][b - 1] == "-" and original_grid[a][b + 1] == "-": # -
    graph[start] = [(start[0], start[1] + 1), (start[0], start[1] - 1)]
    print("-")

if original_grid[a - 1][b] in ["|", "F", "7"] and original_grid[a][b + 1] in ["-", "J", "7"]: # L
    graph[start] = [(start[0] - 1, start[1]), (start[0], start[1] + 1)]
    print("L")

if original_grid[a - 1][b] in ["|", "F", "7"] and original_grid[a][b - 1] in ["-", "L", "F"]: # J
    graph[start] = [(start[0], start[1] - 1), (start[0] - 1, start[1])] 
    print("J")

if original_grid[a + 1][b] in ["|", "L", "J"] and original_grid[a][b - 1] in ["-", "L", "F"]: # 7
    graph[start] = [(start[0] + 1, start[1]), (start[0], start[1] - 1)]
    print("7")

if original_grid[a + 1][b] in ["|", "L", "J"] and original_grid[a][b + 1] in ["-", "J", "7"]: # F
    graph[start] = [(start[0], start[1] + 1), (start[0] + 1, start[1])]
    print("F")


def find_loop(starting_point):
    count = 0
    prev = None
    cur = starting_point
    loop = [starting_point]
    loop_set = set()
    while True:
        for neighbor in graph[cur]:
            if neighbor != prev:
                prev = cur
                cur = neighbor
                loop.append(cur)
                loop_set.add(cur)
                break
        count += 1
        if cur == starting_point:
            break
    
    return loop, loop_set


loop, loop_set = find_loop(start)

new_starting_point = min(loop, key=lambda x: x[1])

print(new_starting_point)

loop, loop_set = find_loop(new_starting_point)

print(loop)

inside = 0

for i, node in enumerate(loop[:-1]):
    if original_grid[node[0] + 1][node[1] + 1] in ["L", "F", "-"]:
        continue
    if original_grid[node[0] + 1][node[1] + 1] == "|" and node[0] < loop[i + 1][0]:
        continue
    if original_grid[node[0] + 1][node[1] + 1] == "J" and node[0] == loop[i + 1][0]:
        continue
    if original_grid[node[0] + 1][node[1] + 1] == "7" and node[1] == loop[i + 1][1]:
        continue
    cur = (node[0], node[1] + 1)
    while cur not in loop_set:
        cur = (cur[0], cur[1] + 1)
        inside += 1

print(inside)