def fibonacci(n):
    answer = 0
    temp_1 = 1
    temp_2 = 1
    for i in range(1, n+1):
        if i == 1:
            answer = temp_1
        elif i == 2:
            answer = temp_2
        else:
            answer = temp_1 + temp_2
            temp_1 = temp_2
            temp_2 = answer

    print(answer)
        
fibonacci(int(input()))