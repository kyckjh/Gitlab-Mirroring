from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(N)]

waters = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == '*':
            waters.append((i, j))
        elif arr[i][j] == 'S':
            start = (i, j)
        elif arr[i][j] == 'D':
            end = (i, j)

q = deque()
q.append(start)

visited = [[0]*M for _ in range(N)]
visited[start[0]][start[1]] = 1
cnt = -1
result = False
while q:
    cnt += 1
    water_len = len(waters)
    for _ in range(water_len):
        wci, wcj = waters.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            wni, wnj = wci+di, wcj+dj
            if 0 <= wni < N and 0 <= wnj < M:
                if arr[wni][wnj] != '.':
                    continue
                arr[wni][wnj] = '*'
                waters.append((wni, wnj))
    q_len = len(q)
    for _ in range(q_len):
        ci, cj = q.popleft()
        if (ci, cj) == end:
            result = True
            break
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] or arr[ni][nj] == '*' or arr[ni][nj] == 'X':
                    continue
                visited[ni][nj] = 1
                q.append((ni, nj))
    if result:
        print(cnt)
        quit()
print('KAKTUS')