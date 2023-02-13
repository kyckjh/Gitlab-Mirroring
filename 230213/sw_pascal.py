T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [1]
    print(f'#{t}')
    for i in range(1, N+1):
        print(*arr)
        temp = [1]
        for n in range(i-1):
            temp.append(arr[n] + arr[n+1])
        temp.append(1)
        arr = temp


