import sys
import copy
def roll(r, c, ss, arr):
    for s in range(1, ss+1):
        i = r-s
        t1 = arr[i][c-s]
        for j in range(c-s, c+s):
            t2 = arr[i][j+1]
            arr[i][j+1] = t1
            t1 = t2
        j = c+s
        for i in range(r-s, r+s):
            t2 = arr[i+1][j]
            arr[i + 1][j] = t1
            t1 = t2
        i = r+s
        for j in range(c+s, c-s, -1):
            t2 = arr[i][j-1]
            arr[i][j-1] = t1
            t1 = t2
        j = c-s
        for i in range(r+s, r-s, -1):
            t2 = arr[i-1][j]
            arr[i-1][j] = t1
            t1 = t2
def perm(cnt):
    global min_v
    if cnt == K:
        arr = copy.deepcopy(origin)
        for order in orders:
            r, c, s = calcs[order]
            roll(r - 1, c - 1, s, arr)
        for i in range(N):
            min_v = min(min_v, sum(arr[i]))
    for i in range(K):
        if select[i] == 1:
            continue
        select[i] = 1
        orders[i] = cnt
        perm(cnt+1)
        select[i] = 0

N, M, K = map(int, sys.stdin.readline().split())
origin = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
calcs = []
for _ in range(K):
    calcs.append(tuple(map(int, sys.stdin.readline().split())))
min_v = float("inf")
orders = [0]*K
select = [0]*K
perm(0)
print(min_v)