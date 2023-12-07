import math

with open("input-day6.txt", "r") as f:
    times, distances = f.readlines()
    time = int(times.split(":")[1].replace(" ", ""))
    distance = int(distances.split(":")[1].replace(" ", ""))

maximum = time / 2 + math.sqrt((time / 2) ** 2 - distance)
if math.floor(maximum) < maximum:
    maximum = math.floor(maximum)
else:
    maximum = math.floor(maximum) - 1
minimum = time / 2 - math.sqrt((time / 2) ** 2 - distance)
if math.ceil(minimum) > minimum:
    minimum = math.ceil(minimum)
else:
    minimum = math.ceil(minimum) + 1
count = maximum - minimum + 1
print(maximum, minimum, count)