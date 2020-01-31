def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num/i == 1:
            break
        elif num % i == 0:
            return False
    return True

num = int(input())
for i in range(num):
    even = int(input())

    numList = list(range(2,even))
    primeList = []
    for i in numList:
        if is_prime(i):
            primeList.append(i)

    tmpList = list(x for x in primeList if x<even)
    result = []

    for i in tmpList:
        tmp = even - i
        if tmp<i:
            break
        if tmp in tmpList:
            result.append((i,tmp))
    """
    if len(result)%2==0:
        index=int(len(result)/2)-1
    else:
        index=int(len(result)/2)
    """
    index = len(result)-1
    print("%d %d" %(result[index][0],result[index][1]))
            

   
