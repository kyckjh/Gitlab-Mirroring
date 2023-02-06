T = int(input())
for t in range(1, T+1):
    arr = [[1]*10 for _ in range(10)]
    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        color += 1
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] *= color
    purple = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j]%6 == 0:
                purple += 1
    print(f'#{t} {purple}')