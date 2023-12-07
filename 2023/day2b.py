with open("input-day2.txt", "r") as f:
    lines = f.readlines()
    result1 = 0
    result2 = 0
    game_no = 1
    for line in lines:
        d = {"green": 0, "blue": 0, "red": 0}
        game, content = line.split(":")
        for game_set in content.split(";"):
            for count_color in game_set.strip().split(","):
                count, color = count_color.strip().split()
                if int(count) > d[color]:
                    d[color] = int(count)
        #if d["red"] <= 12 and d["green"] <= 13 and d["blue"] <= 14:
        #    print(game_no)
        #    result1 += game_no
        result2 += d["red"] * d["blue"] * d["green"]
        game_no += 1
    #print(result1)
    print(result2)    