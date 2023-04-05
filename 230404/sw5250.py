import heapq

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    q = []
    costs = [[0xffffffff]*N for _ in range(N)]
    costs[0][0] = 0
    heapq.heappush(q, (0, 0, 0))
    while q:
        ci, cj, cur_cost = heapq.heappop(q)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            pre_cost = costs[ni][nj]
            new_cost = cur_cost + max(0, arr[ni][nj]-arr[ci][cj]) + 1
            if new_cost < pre_cost:
                costs[ni][nj] = new_cost
                heapq.heappush(q, (ni, nj, new_cost))

    print(f'#{t} {costs[N-1][N-1]}')
'''

3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''