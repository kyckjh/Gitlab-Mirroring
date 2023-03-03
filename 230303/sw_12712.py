import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
for t in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for si in range(N):
        for sj in range(N):
            cnt = arr[si][sj]
            for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                for mul in range(1,M):
                    ni, nj = si+di*mul, sj+dj*mul
                    if 0<=ni<N and 0<=nj<N:
                        cnt += arr[ni][nj]
                ans = max(ans, cnt)
            cnt = arr[si][sj]
            for di, dj in ((-1,-1),(1,1),(1,-1),(-1,1)):
                for mul in range(1,M):
                    ni, nj = si+di*mul, sj+dj*mul
                    if 0<=ni<N and 0<=nj<N:
                        cnt += arr[ni][nj]
                ans = max(ans, cnt)
    print(f'#{t} {ans}')