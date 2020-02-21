N, M = map(int, input().split())

check = [False] * N
arr = []

def back(depth):
    if depth == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(N):
        print("------ %d -----" %(i))
        if check[i]:
            continue
        check[i] = True
        arr.append(i+1)
        print(arr)
        back(depth+1)
        #check[i] = False
        print("pop : %d" %(arr.pop()))
        
        for j in range(i+1, N):
            check[j] = False
            print("make False check[%d]" %(j))
        print(check)

back(0)
    