personNum = int(input())
person = []
result = []
for _ in range(personNum):
    person.append(list(map(int, input().split(' '))))
for me in person:
    count = 1
    for man in person:
        if me[0] < man[0] and me[1] < man[1]:
            count +=1
    result.append(count)

for i in result:
    print("%d " %(i), end='')