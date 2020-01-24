num = int(input())
i=1
count=1
while(True):
    num -= i
    if(num <= 0):
        break
    if i==1:
        i*=6
    else:
        i+=6
    count+=1
print(count)