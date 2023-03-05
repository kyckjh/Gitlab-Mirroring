import sys
papers = [5]*5

def post(i, j, n):
    if i+n > 10 or j+n > 10 or papers[n-1] == 0:
        return False
    for y in range(i, i+n):
        for x in range(j, j+n):
            if arr[y][x] == 0:
                return False
    for y in range(i, i+n):
        for x in range(j, j+n):
            arr[y][x] = 0
    papers[n-1] -= 1
    return True

def depost(i, j, n):
    for y in range(i, i+n):
        for x in range(j, j+n):
            arr[y][x] = 1
    papers[n-1] += 1

def check(): # arr에 1이 없으면 True
    for i in range(10):
        if 1 in arr[i]:
            return False
    return True

def dfs(cnt):
    global ans
    if cnt >= ans:
        return
    if check():
        ans = min(ans, 25-sum(papers))
        return
    for i in range(10):
        for j in range(10):
            if not arr[i][j]:
                continue
            for n in range(5, 0, -1):
                if post(i, j, n): # 붙이는 데 성공하면
                    dfs(cnt+1)
                    depost(i, j, n)
            return
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
ans = float("inf")
dfs(0)
if ans == float("inf"):
    print(-1)
else:
    print(ans)