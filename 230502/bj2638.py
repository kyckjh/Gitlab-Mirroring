import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    airs = [[0]*M for _ in range(N)]
    airs[0][0] = 1
    remove = []
    q = deque()
    q.append((0, 0))

    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci+di, cj+dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or airs[ni][nj] or arr[ni][nj]:
                continue
            airs[ni][nj] = 1
            q.append((ni, nj))

    q.append((0, 0))

    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci+di, cj+dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj]:
                continue
            visited[ni][nj] = 1
            if arr[ni][nj]: # 치즈가 있는 곳이면
                cnt = 0 # 주변의 치즈 개수
                for ddi, ddj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nni, nnj = ni + ddi, nj + ddj
                    # 주변이 공기이면
                    if airs[nni][nnj]:
                        cnt += 1
                if cnt > 1:
                    remove.append((ni, nj))
            else: # 치즈가 없는 곳이면
                q.append((ni, nj))
    result = len(remove)
    for i, j in remove:
        arr[i][j] = 0
    return result


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
remain = 0
for i in range(N):
    remain += sum(arr[i])
ans = 0
while remain > 0:
    remain -= bfs()
    ans += 1

print(ans)