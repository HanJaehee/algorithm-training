def check(board):
    Wcount = 0
    Bcount = 0
    for low in board:
        print(low)
        if low == "W":
            Wcount += 1
        elif low == "B":
            Bcount += 1
    return int(abs(Wcount - Bcount)/2)  

N, M = map(int, input().split())
chess = []
result = 64
for _ in range(N):
    chess.append(input())

for i in range(N-7):
    for j in range(M-7):
        count = 0
        for k in range(i, i+8):
            tmp = []
            for p in range(j, j+8):
                tmp.append(chess[k][p])
            count += check(tmp)
        if result >= count:
            result = count

print(result)