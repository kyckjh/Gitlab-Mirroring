T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = []
    cnt = 0
    for i in [2, 3, 5, 7, 11]:
        while N % i == 0:
            cnt += 1
            N = N // i
        result.append(str(i))
        cnt = 0    
    print(f'#{t}', " ".join(result))