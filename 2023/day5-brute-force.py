import math

with open("input-day5.txt", "r") as f:
    lines = f.readlines()
    seeds = []
    maps = []
    for line in lines:
        if "seeds" in line:
            seeds_and_ranges = list(map(int, line.split(":")[1].strip().split()))
            seeds = seeds_and_ranges[::2]
            ranges = seeds_and_ranges[1::2]
        elif "map" in line:
            maps.append([])
        elif line != "\n":
            dest, src, rang = map(int, line.split())
            maps[-1].append((src, dest, rang))

mappings = []

for mapping in maps:
    intervals = [(-math.inf, math.inf, 0)]
    for src, dest, rang in mapping:
        break_intervals = set()
        for i, interval in enumerate(intervals):
            start, end, change = interval
            if start <= src <= end:
                break_intervals.add(i)
            if start <= src + rang - 1 <= end:
                break_intervals.add(i)
                break
        #print(break_intervals)
        if len(break_intervals) == 1:
            i = break_intervals.pop()
            start, end, change = intervals[i]
            if start < src:
                intervals.insert(i, (start, src - 1, change))
                i = i + 1
            intervals[i] = (src, src + rang - 1, dest - src + change)
            if end > src + rang - 1:
                intervals.insert(i + 1, (src + rang, end, change))
        elif len(break_intervals) == 2:
            i, j = break_intervals
            start1, end1, change1 = intervals[i]
            start2, end2, change2 = intervals[j]
            f = 0
            if start1 < src:
                intervals.insert(i, (start1, src - 1, change1))
                f = 1
            intervals[i + f] = (src, end1, dest - src + change1)
            intervals[j + f] = (start2, src + rang - 1, dest - src + change2)
            if end2 > src + rang - 1:
                intervals.insert(j + f + 1, (src + rang, end2, change2))
            for k in range(i + f + 1, j + f):
                intervals[k] = (intervals[k][0], intervals[k][1], intervals[k][2] + dest - src)
    mappings.append(intervals)
    
with open("intervals.txt", "w") as f:
    f.write(f"{len(seeds)}\n")
    f.write(" ".join(map(str, seeds_and_ranges)) + "\n")
    f.write(f"{len(mappings)}\n")
    for intervals in mappings:
        f.write(f"{len(intervals) - 2} ")
        for start, end, change in intervals[1:-1]:
            f.write(f"{start} {end} {change} ")
        f.write("\n")


def find_key_in_mapping(seed, mapping):
    for src, dest, rang in mapping:
        if src <= seed <= src + rang - 1:
            #print("matched", src, dest, rang)
            return seed - src + dest
    #print("no match found")
    return seed

def find_location(seed):
    tmp = seed
    #print(f"find seed {seed} in the maps")
    #for mapping in maps:
        #tmp = find_key_in_mapping(tmp, mapping)
        #print("intermediate result:", tmp)
    
    for intervals in mappings:
        for start, end, change in intervals:
            if start <= seed <= end:
                tmp = tmp + change
                break
    return tmp

min_location = math.inf

"""
for first_seed in seeds:
    for rang in ranges:
        for seed in range(first_seed, first_seed + rang):
            loc = find_location(seed)
            if loc < min_location:
                min_location = loc

"""
                
for seed, rang in zip(seeds, ranges):
    print("starting seed", seed)
    percentage = 0
    for i in range(seed, seed + rang):
        loc = find_location(i)
        if loc < min_location:
            min_location = loc
        if (i - seed) * 100 // rang > percentage:
            percentage += 1
            print(percentage)
    print("done range")

print(min_location)
