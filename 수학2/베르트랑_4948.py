def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num/i == 1:
            break
        elif num % i == 0:
            return False
    return True

numList = list(range(2,246912))
primeList = []

for i in numList:
    if is_prime(i):
        primeList.append(i)

while True:
    n = int(input())
    if n==0:
        break
    count=0
    for i in primeList:
        if n < i <= n*2:
            count+=1
    print(count)
    
   
