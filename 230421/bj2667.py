import sys
from collections import deque

input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    result = 1
    arr[i][j] = '0'
    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '1':
                arr[ni][nj] = '0'
                result += 1
                q.append((ni, nj))
    return result


N = int(input())
arr = [list(input().strip()) for _ in range(N)]
results = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            results.append(bfs(i, j))

results.sort()
print(len(results))
for result in results:
    print(result)