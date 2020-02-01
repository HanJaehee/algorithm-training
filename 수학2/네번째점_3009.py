def func(a1,a2,a3):
    if a1==a2:
        return a3
    elif a2==a3:
        return a1
    else:
        return a2

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

print("%d %d" %(func(x1,x2,x3), func(y1, y2, y3)))

