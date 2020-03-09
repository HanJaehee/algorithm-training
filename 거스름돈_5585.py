price = 1000 - int(input())
result = 0

def calc(price, val):
    result = 0
    if price >= val:
        result += int(price/val)
        price %= val
    return price, result

for i in [500, 100, 50, 10, 5, 1]:
    price, tmp = calc(price, i)
    result += tmp

print(result)
    