x,y,w,h = map(int, input().split())
a = []
a.append(x)
a.append(y)
a.append(w-x)
a.append(h-y)
print(min(a))
