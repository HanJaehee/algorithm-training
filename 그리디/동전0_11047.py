N, K = map(int, input().split(' '))
val = []
for _ in range(N):
    val.append(int(input()))
val.reverse()

count = 0
for num in val:
    if K%num != K:
        count += K//num
        K = K%num
print(count)