from sys import stdin
from collections import deque
input = stdin.readline

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

q = deque()
ans = 0
q.append((0, 0, 0, K))
dir1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dir2 = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-2, -1), (1, -2), (2, -1)]
#visited = [[0]*W for _ in range(H)]
ans = 10**9
while q:
    ci, cj, cnt, chance = q.popleft()
    if ci == H-1 and cj == W-1:
        ans = min(ans, cnt)
    if chance > 0:
        for di, dj in dir2:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < H and 0 <= nj < W:
                if arr[ni][nj]:
                    continue
                arr[ni][nj] = 1
                q.append((ni, nj, cnt+1, chance-1))
    for di, dj in dir1:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < H and 0 <= nj < W:
            if arr[ni][nj]:
                continue
            arr[ni][nj] = 1
            q.append((ni, nj, cnt+1, chance))
if ans == 10**9:
    print(-1)
else:
    print(ans)