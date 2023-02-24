import sys
sys.stdin = open("input.txt", "r")

def bfs(i, j):
    queue = []
    cnt = 1
    queue.append((i, j, cnt))

    while queue:
        ci, cj, cnt = queue.pop(0)
        for y, x in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci + y, cj + x
            if 0<=ni<N and 0<=nj<N and (arr[ni][nj] - arr[ci][cj]) == 1:
                queue.append((ni, nj, cnt+1))
    return cnt


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    max_v = 0
    for i in range(N):
        for j in range(N):
            value = bfs(i, j)
            if max_v < value:
                ans = arr[i][j]
                max_v = value
            if max_v == value:
                if ans > arr[i][j]:
                    ans = arr[i][j]
    print(f'#{t} {ans} {max_v}')
