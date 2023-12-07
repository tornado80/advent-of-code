with open("input-day4.txt", "r") as f:
    result = 0
    for line in f.readlines():
        winning, oma = line.split(":")[1].split("|")
        winning = winning.strip().split()
        oma = oma.strip().split()
        points = 0
        for number in oma:
            if number in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        result += points
    print(result)