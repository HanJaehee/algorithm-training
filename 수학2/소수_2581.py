num_M = int(input())
num_N = int(input())

sum=0
minimum=0
for i in range(num_M, (num_N+1)):
    count=0
    for j in range(1, i+1):
        if i%j==0:
            count += 1
    if count == 2:
        sum+=i
        if minimum ==0:
            minimum = i
            
if sum==0 and minimum ==0:
    print(-1)
else:
    print(sum)
    print(minimum)