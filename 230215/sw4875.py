def dfs(sr, sc):
    stack = []
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    # 위쪽부터 시계방향으로 확인
    dr = [-1, 0, 1, 0]  
    dc = [0, 1, 0, -1] 
    for d in range(4): # 처음 시작위치 기준 4방향 모두 확인
        nr, nc = sr + dr[d], sc + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and not visited[nr][nc]:
            stack.append((nr, nc, d))   # 갈 수 있는 위치가 주변에 있으면 위치와 방향 스택에 저장
            visited[nr][nc] = 1 # 스택에 있는 곳은 무조건 방문할것이므로 방문표시
    while stack:
        cr, cc, cd = stack.pop() # 스택의 top에 있는 곳의 위치와 방향 pop 하면서 저장
        if arr[cr][cc] == 3:     # 현재 위치가 목적지면 1 리턴
            return 1
        for d in range(cd-1, cd+2): # 내가 왔던 방향 제외하고 3방향 확인
            nr, nc = cr + dr[d%4], cc + dc[d%4] # 인덱스 벗어나지 않도록 4로 모듈러 연산
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and not visited[nr][nc]:
                # 갈 수 있는 위치면 위치 및 방향 스택에 저장
                stack.append((nr, nc, d))
                visited[nr][nc] = 1
    return 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # int 형태로 arr에 저장, error 방지 위해 strip() 사용
    arr = [list(map(lambda x: int(str(x)), input().strip())) for _ in range(N)]
    end = False

    for i in range(N):
        if 2 in arr[i]: # 행마다 2(출발점)가 있는지 확인
            print(f'#{t} {dfs(i, arr[i].index(2))}') # 2를 찾으면 찾은 행과 2가 있는 열부터 시작
            break

'''
5
6
101011
101011
101012
100000
301110
101000
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
5
11111
11111
11111
11112
11112
5
00000
00000
00000
00000
00202
'''