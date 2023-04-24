import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0]*(N+1)
    visited[start] = 1
    while q:
        now, cnt = q.popleft()
        for next in arr[now]:
            if visited[next]:
                continue
            visited[next] = 1
            frs[start] += cnt+1
            q.append((next, cnt+1))

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

frs = [0]*(N+1)
for i in range(1, N+1):
    bfs(i)
min_v = min(frs[1:])
print(frs.index(min_v))
