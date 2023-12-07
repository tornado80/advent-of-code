with open("input-day4.txt", "r") as f:
    win = []
    lines = f.readlines()
    n = len(lines)
    for line in lines:
        winning, oma = line.split(":")[1].split("|")
        winning = winning.strip().split()
        oma = oma.strip().split()
        points = 0
        for number in oma:
            if number in winning:
                points += 1
        win.append(points)

dp = [0 for _ in range(n)]
for i in range(n - 1, -1, -1):
    dp[i] = 1
    j = 1
    while j <= win[i] and i + j < n:
        dp[i] += dp[i + j]
        j += 1
print(sum(dp))