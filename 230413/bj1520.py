import sys
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(i, j):
    if ways[i][j] != -1:
        return ways[i][j]
    result = 0
    for k in range(4):
        ni, nj = i+dy[k], j+dx[k]
        if 0 <= ni < M and 0 <= nj < N:
            if arr[i][j] > arr[ni][nj]:
                ways[ni][nj] = dfs(ni, nj)
                result += ways[ni][nj]
    return result

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
ways = [[-1]*N for _ in range(M)]
ways[M-1][N-1] = 1
result = dfs(0, 0)
print(result)