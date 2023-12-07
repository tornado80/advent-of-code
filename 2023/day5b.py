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

final_mapping = [(-math.inf, math.inf, 0)]

for mapping in mappings:
    new_final_mapping = []
    for start, end, change in final_mapping:
        true_start = start + change
        true_end = end + change
        sub_final_mapping = []
        for m_start, m_end, m_change in mapping:
            if m_start <= true_start and true_end <= m_end:
                sub_final_mapping.append((start, end, change + m_change))
                break
            if m_start <= true_start <= m_end:
                sub_final_mapping.append((start, m_end - change, change + m_change))
            if true_start < m_start and m_end < true_end:
                sub_final_mapping.append((m_start - change, m_end - change, change + m_change))
            if m_start <= true_end <= m_end:
                sub_final_mapping.append((m_start - change, end, change + m_change))
                break
        if len(sub_final_mapping) == 0:
            new_final_mapping.append((start, end, change))
        else:
            new_final_mapping.extend(sub_final_mapping)
    final_mapping = new_final_mapping

min_location = math.inf
                
for seed, rang in zip(seeds, ranges):
    start = seed
    end = seed + rang - 1
    for f_start, f_end, f_change in final_mapping:
        if f_start <= start and end <= f_end:
            min_location = min(min_location, start + f_change, end + f_change)
            break
        if f_start <= start <= f_end:
            min_location = min(min_location, start + f_change, f_end + f_change)
        if start < f_start and f_end < end:
            min_location = min(min_location, f_start + f_change, f_end + f_change)
        if f_start <= end <= f_end:
            min_location = min(min_location, f_start + f_change, end + f_change)
            break

print(min_location)
