N = int(input())
data = [[0]*(N) for _ in range(N)]

for i in range(N):
    tmp = input()
    for j in range(N):
        data[i][j] = int(tmp[j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs(cnt, a, b):
    data[a][b]=0
    for i in range(4):
        ax = a + dx[i]
        ay = b + dy[i]
        if ax>=0 and ax<N and ay>=0 and ay<N:
            if data[ax][ay] == 1:
                cnt = dfs(cnt+1, ax, ay)
    return cnt

ans = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            ans.append(dfs(1, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)