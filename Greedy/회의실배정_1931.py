num = int(input())
time = []

for _ in range(num):
    a = list(map(int, input().split()))
    time.append(a)

meeting = sorted(time, key=lambda time: time[0])
meeting = sorted(meeting, key=lambda meeting: meeting[1])
count = 0
start = 0

for time in meeting:
    if time[0]>=start:
        start = time[1]
        count+=1
print(count)