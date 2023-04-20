import sys
from collections import deque
input = sys.stdin.readline

def bfs1(i, j):
    q = deque()
    q.append((i, j))
    result = [(i, j)]
    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj]:
                visited[ni][nj] = 1
                result.append((ni, nj))
                q.append((ni, nj))
    return result



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
islands = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = 1
            islands.append(bfs1(i, j))

ans = 10**9
for island in islands:
    visited = [[0] * N for _ in range(N)]
    q = deque()
    for i, j in island:
        visited[i][j] = 1
        q.append((i, j, 0))

    while q:
        ci, cj, cnt = q.popleft()
        if arr[ci][cj] == 1 and cnt != 0:
            ans = min(ans, cnt)
            break
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj, cnt+1))

print(ans-1)