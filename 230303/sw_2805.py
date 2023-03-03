T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    ans = 0
    m = N//2
    for i in range(N):
        for j in range(abs(m-i), N-abs(m-i)):
            ans += arr[i][j]
    print(f'#{t} {ans}')