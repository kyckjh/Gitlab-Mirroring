import sys
sys.setrecursionlimit(10**6)
def land(y, x):
    if arr[y][x] != 1:
        return
    arr[y][x] = 2
    for k in range(8):
        land(y+dy[k], x+dx[k])

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break
    arr = [[2] * (w+2)]
    for _ in range(h):
        arr.append([2]+list(map(int, input().split()))+[2])
    arr.append([2]*(w+2))
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    ans = 0
    for i in range(1, h+2):
        for j in range(1, w+2):
            if arr[i][j] == 1:
                ans += 1
                land(i, j)
    print(ans)