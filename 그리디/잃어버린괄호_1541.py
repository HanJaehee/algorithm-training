formula = input()
tmp = list(formula.split('-'))
result = []
for i in tmp:
    tmp_sum = 0
    if "+" in i:
        temp = i.split('+')
        for j in temp:
            tmp_sum += int(j)
        result.append(tmp_sum)
    else:
        result.append(int(i)) 
print(result[0] - sum(result[1:]))