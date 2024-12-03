import re

def part1():
    with open("03.txt") as f:
        lines = f.readlines()
        s = 0
        for line in lines:
            all_matches = re.findall(r"mul\((\d{1,3})\,(\d{1,3})\)", line)
            for left, right in all_matches:
                s += int(left) * int(right)
        print(s)

def part2(line, state):
    s = 0
    all_matches = re.findall(r"(?P<do>do\(\))|(?P<dont>don\'t\(\))|mul\((?P<left>\d{1,3})\,(?P<right>\d{1,3})\)", line)
    print(all_matches)
    for (do, dont, left, right) in all_matches:
        if do == "do()":
            state = 1
        elif dont == "don't()":
            state = 0
        elif state == 1:
            print(left, right)
            s += int(left) * int(right)
    print(s)
    return s, state

part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 1)

with open("03.txt") as f:
    lines = f.readlines()
    s = 0
    state = 1
    for line in lines:
        sd, state = part2(line, state)
        s += sd
    print(s)