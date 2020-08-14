N, M = map(int, input().split(' '))
card = list(map(int, input().split(' ')))
result = 0

for i in range(len(card)):
    for j in range((i+1), len(card)):
        for k in range((j+1), len(card)):
            tmp1 = card[i] + card[j] + card[k]
            if tmp1 >= result and tmp1 <= M:
                result = tmp1
print(result)