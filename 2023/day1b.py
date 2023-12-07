d = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

with open("input-day1.txt", "r") as f:
    result = 0
    line_no = 1
    for line in f.readlines():
        lindex = len(line)
        lvalue = 0

        rindex = -1
        rvalue = 0

        for key, value in d.items():
            li = line.find(key)
            ri = line.rfind(key)
            if li != -1 and li < lindex:
                lindex = li
                lvalue = value
                lkey = key
            if ri != -1 and ri > rindex:
                rindex = ri
                rvalue = value
                rkey = key
        n = lvalue * 10 + rvalue
        print(f"{line_no}. {n}") # {lkey} at {lindex} and {rkey} at {rindex} = 
        line_no += 1
        """
        for i in range(len(line)):
            if line[i].isdigit():
                n = int(line[i]) * 10
                break
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                n += int(line[i])
                break
        """
        result += n
    print(result)