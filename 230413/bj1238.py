import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(target, graph):
    q = []
    heappush(q, (0, target))
    costs = [float("inf")] * (N + 1)
    costs[target] = 0
    while q:
        cost, now = heappop(q)
        if cost > costs[now]:
            continue
        for i in range(N+1):
            next_cost = cost + graph[now][i]
            if graph[now][i] != 0:
                if costs[i] > next_cost:
                    costs[i] = next_cost
                    heappush(q, (next_cost, i))
    return costs

N, M, X = map(int, input().split())
graph1 = [[0]*(N+1) for _ in range(N+1)]
graph2 = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph1[a][b] = t
    graph2[b][a] = t

costs1 = dijkstra(X, graph1)
costs2 = dijkstra(X, graph2)

max_v = 0
for i in range(1, N+1):
    max_v = max(max_v, costs1[i]+costs2[i])
print(max_v)