import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    in_degree[b] += 1

q = deque()
visited = [0]*(N+1)
for i in range(1, N+1):
    if not in_degree[i]:
        q.append(i)
        visited[i] = 1
ans = []
while q:
    now = q.popleft()
    ans.append(now)
    for next in arr[now]:
        if visited[next]:
            continue
        in_degree[next] -= 1
        if not in_degree[next]:
            q.append(next)
            visited[next] = 1

print(*ans)
