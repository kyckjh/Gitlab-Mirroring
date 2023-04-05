import heapq

T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[0xffffffff] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    U = set()
    q = []
    weight = [0xffffffff] * (N+1)
    weight[0] = 0
    heapq.heappush(q, (0, 0))
    while len(U) < N+1:
        w, idx = heapq.heappop(q)
        U.add(idx)
        for i in range(N+1):
            if i in U:
                continue
            if weight[i] > graph[idx][i] + w:
                weight[i] = graph[idx][i] + w
                heapq.heappush(q, (graph[idx][i] + w, i))
    print(f'#{t} {weight[N]}')

'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''