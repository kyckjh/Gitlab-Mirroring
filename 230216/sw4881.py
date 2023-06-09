def f(i, k, preSum):
    global minSum
    if preSum > minSum:
        return
    if i == k:
        minSum = preSum
    else:
        for j in range(i, k):
           p[i], p[j] = p[j], p[i]
           f(i+1, k, preSum + arr[i][p[i]])
           p[i], p[j] = p[j], p[i]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    p = list(range(N))
    arr = [list(map(int, input().split())) for _ in range(N)]
    minSum = 10*N
    f(0, N, 0)
    print(f'#{t} {minSum}')