import sys
input = sys.stdin.readline
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N = int(input())
K = int(input())
arr = [[-1]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input())
    arr[a-1][b-1] = -2
L = int(input())
tail = (0, 0)
head = (0, 0)
now_dir = 1
arr[0][0] = 1
pre = 0
result = True
time = 0
for _ in range(L):
    X, C = input().split()
    X = int(X)
    while time < X:
        time += 1
        next_dir = arr[head[0]][head[1]]
        nhi, nhj = head[0]+dir[next_dir][0], head[1]+dir[next_dir][1]
        if nhi < 0 or nhi >= N or nhj < 0 or nhj >= N or arr[nhi][nhj] > 0:
            result = False
            break
        elif arr[nhi][nhj] == -1:
            next_dir = arr[tail[0]][tail[1]]
            arr[tail[0]][tail[1]] = -1
            tail = (tail[0]+dir[next_dir][0], tail[1]+dir[next_dir][1])        
        arr[nhi][nhj] = now_dir
        head = (nhi, nhj)
    if not result:
        break
    pre = X
    if C == 'D':
        now_dir = (now_dir+1)%4
    else:
        now_dir = (now_dir+3)%4
print(time)