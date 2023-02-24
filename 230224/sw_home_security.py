import sys
sys.stdin = open("sample_input.txt", "r")

cost = [k*k+(k-1)*(k-1) for k in range(41)]
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def bfs(i, j):
    visited = [[0]*N for _ in range(N)]
    results = [0] * (N * 2 + 1)
    queue = [(i, j, 1)]
    visited[i][j] = 1
    while queue:
        ci, cj, k = queue.pop(0)
        results[k] += arr[ci][cj]
        for dy, dx in dir:
            ny, nx = ci + dy, cj + dx
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                visited[ny][nx] = 1
                queue.append((ny, nx, k+1))
    costs = results[:]
    for i in range(1, len(costs)):
        costs[i] *= M
        costs[i] += costs[i-1]
    for i in range(1, len(costs)):
        costs[i] -= cost[i]
    ans = 0
    for i in range(len(results)-1, 0, -1):
        if costs[i] >= 0:
            for j in range(i, 0, -1):
                ans += 1 * results[j]
            break
    return ans

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
             result = bfs(i, j)
             if result > max_v:
                 max_v = result
    print(f'#{t} {max_v}')

'''
1
5 1
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
'''