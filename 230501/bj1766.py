import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
topo = [0]* (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    topo[B] += 1

q = []
for i in range(1, N+1):
    if not topo[i]:
        heappush(q, i)
ans = []
while q:
    now = heappop(q)
    ans.append(now)
    for next in graph[now]:
        topo[next] -= 1
        if topo[next] == 0:
            heappush(q, next)

print(*ans)