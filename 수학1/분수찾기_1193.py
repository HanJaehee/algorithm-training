num = int(input())
i = 1
while(True):
    if (num-i)<=0:
        break
    else:
        num -= i
    i += 1
son = i+1
if i%2 == 1:
    print("%d/%d" %(son-num, num))
else:
    print("%d/%d" %(num, son-num))