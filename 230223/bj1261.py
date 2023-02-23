import sys

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
distance = [[10000000]*M for _ in range(N)]
distance[0][0] = 0
queue = []
#visited = [[0]*M for _ in range(N)]
queue.append((0, 0))
while queue:
    cy, cx = queue.pop(0)
    for k in range(4):
        ny = cy + dy[k]
        nx = cx + dx[k]
        if 0 <= ny < N and 0 <= nx < M:# and visited[ny][nx] == 0:
            origin = distance[ny][nx]
            new = distance[cy][cx] + arr[ny][nx]
            #visited[ny][nx] = 1
            if new < origin:
                distance[ny][nx] = new
                queue.append((ny, nx))

# for i in range(N):
#     for j in range(M):
#         for k in range(4):
#             ny = i + dy[k]
#             nx = j + dx[k]
#             if 0 <= ny < N and 0 <= nx < M:
#                 origin = distance[ny][nx]
#                 new = distance[i][j] + arr[ny][nx]
#                 if new < origin:
#                     distance[ny][nx] = new
print(distance[N-1][M-1])

'''
3 1
010
'''