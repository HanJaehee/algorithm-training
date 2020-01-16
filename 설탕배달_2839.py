A=int(input())

tmp = A/5
min = 10000
for i in range(int(tmp)+1):
    tmp1 = A-5*i
    val2 = int(tmp1/3)
    if tmp1%3==0:
        if min > (i+val2):
            min = i+val2
if min == 10000:
    print(-1)
else:    
    print(min)