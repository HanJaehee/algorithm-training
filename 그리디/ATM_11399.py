num = int(input())
time = list(map(int, input().split()))
time = sorted(time)
result = 0

for i in time:
    result += i*num
    num -= 1
print(result)