import sys
input = sys.stdin.readline

def dfs(pre, sum_w, sum_v):
    global ans
    for i in range(pre+1, N):
        nw = sum_w + arr[i][0]
        if selected[i] or nw > K:
            continue
        selected[i] = 1
        nv = sum_v + arr[i][1]
        dfs(i, nw, nv)
        selected[i] = 0
    ans = max(ans, sum_v)

N, K = map(int, input().split())
arr = []
selected = [0]*N
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
ans = 0
dfs(-1, 0, 0)
print(ans)

'''
6 304
98 98
4 4
6 6
100 100
101 101
103 103

'''