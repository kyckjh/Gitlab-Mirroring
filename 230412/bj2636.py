from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj]:
                    surf.append((ni, nj))
                else:
                    q.append((ni, nj))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
hours = 0
nums = 0
while True:
    visited = [[0]*M for _ in range(N)]
    surf = []
    for i in range(N):
        if not visited[i][0]:
            bfs(i, 0)
        if not visited[i][M-1]:
            bfs(i, M-1)
    for i in range(1, M-1):
        if not visited[0][i]:
            bfs(0, i)
        if not visited[N-1][i]:
            bfs(N-1, i)
    if not surf:
        break
    nums = len(surf)
    hours += 1
    for y, x in surf:
        arr[y][x] = 0
print(hours, nums)