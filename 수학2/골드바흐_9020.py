def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num/i == 1:
            break
        elif num % i == 0:
            return False
    return True

def func(even):
    tmpList = list(x for x in primeList if even>=x)
    result = []
    for x in range(int(len(tmpList)/2),-1,-1):
        tmp = even - tmpList[x]
        if tmp in tmpList:
            return [tmp,tmpList[x]] if tmp<tmpList[x] else [tmpList[x],tmp] 

numList = list(range(2,10000))
primeList = []

for i in numList:
    if is_prime(i):
        primeList.append(i)

for _ in range(int(input())):
    val = func(int(input()))
    print("%d %d" %(val[0], val[1]))
