with open("input-day9.txt") as f:
    sequences = []
    for line in f.readlines():
        sequences.append(list(map(int, line.strip().split())))

s1 = 0
s2 = 0
for sequence_number, sequence in enumerate(sequences):
    last_numbers = [sequence[-1]]
    first_numbers = [sequence[0]]
    while True:
        print(sequence)
        differences = []
        zero_count = 0
        for i in range(len(sequence) - 1):
            difference = sequence[i + 1] - sequence[i]
            if difference == 0:
                zero_count += 1
            differences.append(difference)
        if zero_count == len(sequence) - 1:
            break
        first_numbers.append(differences[0])
        last_numbers.append(differences[-1])
        sequence = differences
    for i in range(len(last_numbers) - 2, -1, -1):
        last_numbers[i] = last_numbers[i] + last_numbers[i + 1]
    for i in range(len(first_numbers) - 2, -1 , -1):
        first_numbers[i] = first_numbers[i] - first_numbers[i + 1]
    s1 += last_numbers[0]
    s2 += first_numbers[0]
    print(sequence_number + 1, last_numbers[0], first_numbers[-1])
print(s1, s2)