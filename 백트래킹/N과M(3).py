N, M = map(int, input().split())

check = [False] * N
arr = []

def back(depth):
    if depth == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(N):
        if check[i]:
            continue
        arr.append(i+1)
        back(depth+1)
        arr.pop()
        
        for j in range(i+1, N):
            check[j] = False


back(0)
    