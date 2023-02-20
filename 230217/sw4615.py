T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0]*(N+2) for _ in range(N+2)]
    m = N//2
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m][m+1] = arr[m+1][m] = 1

    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            tlst = []
            for mul in range(1, N):
                ni, nj = si+di*mul, sj+dj*mul
                if arr[ni][nj]==0:
                    break
                elif arr[ni][nj] != d:
                    tlst.append((ni, nj))
                else:
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break
        bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{t} {bcnt} {wcnt}')


'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2'''
