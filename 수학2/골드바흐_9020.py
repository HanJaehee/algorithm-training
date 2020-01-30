def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num/i == 1:
            break
        elif num % i == 0:
            return False
    return True

numList = list(range(2,10000))
primeList = []

for i in numList:
    if is_prime(i):
        primeList.append(i)

print(primeList)

num = int(input())
for i in range(num):
    even = int(input())
    tmpList = list(
    https://stackoverflow.com/questions/9138112/looping-over-a-list-in-python
   
