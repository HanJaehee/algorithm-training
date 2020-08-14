num = int(input())
i=0
while i != num:
    numSum = list(map(int, str(i)))
    tmp = i + sum(numSum)
    if tmp == num:
        print(i)
        break
    if i == num-1:
        print(0)
    i += 1
