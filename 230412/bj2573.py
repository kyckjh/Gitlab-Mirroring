import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def check():
    result = 0    
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] > 0:
                visited[i][j] = 1
                result += dfs(i, j)
                return result+1
    return 0

def dfs(i, j):
    result = 0
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if arr[i+di][j+dj] > 0 and not visited[i+di][j+dj]:
            result += 1
            visited[i+di][j+dj] = 1
            result += dfs(i+di, j+dj)
    return result


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
days = 0
while True:
    lst = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    days += 1
    nums = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            cnt = 0
            if arr[i][j] > 0:
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if arr[i+di][j+dj] < 1:
                        cnt += 1
                    lst[i][j] = cnt
    for i in range(1, N-1):
        for j in range(1, M-1):
            arr[i][j] -= lst[i][j]
            if arr[i][j] > 0:
                nums+=1
    
    result = check()
    if result == 0:
        days = 0
        break
    if result < nums:
        break
    if result == nums:
        continue
print(days)