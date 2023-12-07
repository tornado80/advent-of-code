import functools

with open("input-day7.txt", "r") as f:
    l = []
    for line in f.readlines():
        hand, num = line.split()
        l.append((hand, int(num)))

def find_frequencies(word):
    d = {}
    for char in word:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

def hand_type(hand: str):
    d = find_frequencies(hand)
    l = sorted(d.items(), key=lambda x: x[1], reverse=True)
    if l[0][1] == 5:
        return 6 # five of a kind
    elif l[0][1] == 4:
        return 5 # four of a kind
    elif l[0][1] == 3:
        if l[1][1] == 2:
            return 4 # full house
        else:
            return 3 # three of a kind
    elif l[0][1] == 2:
        if l[1][1] == 2:
            return 2 # two pairs
        else:
            return 1 # one pair
    else:
        return 0 # high card    

def best_hand_type(hand: str):
    maximum = -1
    for alternative in ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
        new_hand = hand.replace(alternative, 'J')
        if hand_type(new_hand) > maximum:
            maximum = hand_type(new_hand)
    return maximum

@functools.cmp_to_key
def cmp(hand1, hand2):
    d = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, 
         '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, 
         '2': 2, 'J': 1}
    h1 = best_hand_type(hand1[0])
    h2 = best_hand_type(hand2[0])
    if h1 != h2:
        return -1 if h1 < h2 else 1
    else:
        for i in range(5):
            if d[hand1[0][i]] != d[hand2[0][i]]:
                return -1 if d[hand1[0][i]] < d[hand2[0][i]] else 1
        return 0

l.sort(key=cmp)

s = 0 
for i in range(1, len(l) + 1):
    print(l[i - 1])
    s += l[i - 1][1] * i

print(s)