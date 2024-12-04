directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

xmas = ['X', 'M', 'A', 'S']

def is_xmas(lines, i, j, d):
    for k in range(len(xmas)):
        x = i + d[0] * k
        y = j + d[1] * k
        if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[i]):
            return False
        if lines[x][y] != xmas[k]:
            return False
    return True

def part1(lines):
    count = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines)):
            if lines[i][j] == 'X':
                print("candidate", i, j)
                for d in directions:
                    if is_xmas(lines, i, j, d):
                        count += 1
                        print(i, j, d)
    print(count)
    return count

def is_Xmas(lines, i, j):
    if i < 1 or i >= len(lines) - 1 or j < 1 or j >= len(lines[i]) - 1:
        return False
    if not (lines[i + 1][j + 1] == 'M' and lines[i - 1][j - 1] == 'S') and not (lines[i + 1][j + 1] == 'S' and lines[i - 1][j - 1] == 'M'):
        return False
    if not (lines[i + 1][j - 1] == 'M' and lines[i - 1][j + 1] == 'S') and not (lines[i + 1][j - 1] == 'S' and lines[i - 1][j + 1] == 'M'):
        return False
    return True

def part2(lines):
    count = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines)):
            if lines[i][j] == 'A':
                print("candidate", i, j)
                if is_Xmas(lines, i, j):
                    count += 1
                    print(i, j)
    print(count)
    return count

with open("04.txt", "r") as f:
    lines = f.read().splitlines()

lines1 = """..X...
.SAMX.
.A..A.
XMAS.S
.X....""".splitlines()

lines2 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

part2(lines)