import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    home = tuple(map(int, input().split()))
    arr = []
    visited = [0]*n
    for _ in range(n):
        arr.append(tuple(map(int, input().split())))
    rockx, rocky = map(int, input().split())
    q = deque()
    q.append(home)
    result = True
    while q:
        cx, cy = q.popleft()
        if abs(cx-rockx)+abs(cy-rocky)<=1000:
            print('happy')
            result = False
            break
        for i in range(n):
            nx, ny = arr[i]
            if visited[i] or abs(cx-nx)+abs(cy-ny)>1000:
                continue
            visited[i] = 1
            q.append(arr[i])
    if result:
        print('sad')