with open("2023/input-day8.txt") as f:
    lines = f.readlines()
    instructions = lines[0].strip()
    mapping = {}
    for i in range(2, len(lines)):
        mapping[lines[i][:3]] = (lines[i][7:10], lines[i][12:15])

def find_reachables(cur):
    j = 0
    count = 0
    reachables = {}
    while True:
        instruction = instructions[j]
        count += 1
        if instruction == "L":
            cur = mapping[cur][0]
        else:
            cur = mapping[cur][1]
        if cur.endswith("Z"):
            if (cur, j) not in reachables:
                reachables[(cur, j)] = count
            else:
                print("stopped at", count, cur, j)
                break
        j += 1
        if j == len(instructions):
            j = 0
    return reachables

cur = [node for node in mapping.keys() if node.endswith("A")]

for node in cur:
    print(node)
    print(find_reachables(node))

# with the following result, the solution is lcm of these numbers
"""
FDA
{('HJZ', 0): 19199}
BPA
{('SBZ', 0): 11309}
BVA
{('RFZ', 0): 17621}
NDA
{('VPZ', 0): 20777}
AAA
{('ZZZ', 0): 16043}
QCA
{('PQZ', 0): 15517}
"""
# no need to do the simulation, just find the lcm of these numbers
"""
count = 0
j = 0
flag = 0
max_flag = 0
while flag < len(cur):
    instruction = instructions[j]
    j += 1
    count += 1
    if j == len(instructions):
        j = 0
    flag = 0
    for k in range(len(cur)):
        if instruction == "L":
            cur[k] = mapping[cur[k]][0]
        else:
            cur[k] = mapping[cur[k]][1]
        if cur[k].endswith("Z"):
            flag += 1
    if flag > max_flag:
        max_flag = flag
print(cur, count)
"""