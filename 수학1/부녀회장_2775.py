case = int(input())
for i in range(case):
    a = int(input())
    b = int(input())
    c=[]
    for i in range(1, (b+1)):
        c.append(i)
    for i in range(a):
        tmp = c[:]
        del c[:]
        for i in range(1, len(tmp)+1):
            result=0
            for k in range(0, i):
                result+=tmp[k]
            c.append(result)
    print(c[b-1])