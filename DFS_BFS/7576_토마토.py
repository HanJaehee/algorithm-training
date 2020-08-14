import sys
from collections import deque

r = sys.stdin.readline
x, y = map(int, r().split())

data, tomato = [], deque()

for i in range(y):
    tmp = list(map(int, r().split(' ')))
    for j in range(x):
        if tmp[j] == 1:
            tomato.append([i,j])
    data.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = -1

while tomato:
    for _ in range(len(tomato)):
        b, a = tomato.popleft()
        for i in range(4):
            ax = a + dx[i]
            ay = b + dy[i]
            if (0 <= ax < x) and (0<= ay < y) and (data[ay][ax] == 0):
                tomato.append([ay, ax])
                data[ay][ax] = 1

    cnt += 1

for tmp in data:
    if 0 in tmp:
        cnt = -1
print(cnt)

