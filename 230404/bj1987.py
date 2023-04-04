import sys
input = sys.stdin.readline

def dfs(ci, cj, cnt):
    global ans
    ans = max(ans, cnt)
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = ci+di, cj+dj
        if 0 <= ni < R and 0 <= nj < C:
            if check[arr[ni][nj]]:
                continue
            check[arr[ni][nj]] = 1
            dfs(ni, nj, cnt+1)
            check[arr[ni][nj]] = 0

R, C = map(int, input().split())
arr = [list(map(lambda x: ord(str(x))-65, input().strip())) for _ in range(R)]
ans = 0
check = [0]*26
check[arr[0][0]] = 1
dfs(0, 0, 0)
print(ans+1)