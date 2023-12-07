import math

with open("input-day5.txt", "r") as f:
    lines = f.readlines()
    seeds = []
    maps = []
    for line in lines:
        if "seeds" in line:
            seeds = list(map(int, line.split(":")[1].strip().split()))
        elif "map" in line:
            maps.append([])
        elif line != "\n":
            dest, src, rang = map(int, line.split())
            maps[-1].append((src, dest, rang))

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
    for mapping in maps:
        tmp = find_key_in_mapping(tmp, mapping)
        #print("intermediate result:", tmp)
    return tmp


min_location = math.inf

for seed in seeds:
    loc = find_location(seed)
    if loc < min_location:
        min_location = loc

print(min_location)

