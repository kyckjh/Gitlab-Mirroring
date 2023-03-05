import sys
def bfs(i, j, visited):
    visited[i][j] = 1   # 바이러스 원점 방문
    result = 1
    queue = []
    queue.append((i, j))
    while queue:
        ci, cj = queue.pop(0)
        # 현재 칸 기준으로 상하좌우 4방향 탐색
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            # 범위 안에 있고 빈 칸(0)이고 바이러스가 아직 퍼지지 않았으면
            if 0<=ni<N and 0<=nj<M and not arr[ni][nj] and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = 1 # 방문(바이러스가 퍼짐)
                result += 1         # 바이러스가 퍼진 곳 개수 더하기
    return result   # 바이러스가 퍼진 곳 개수 반환

# cnt : 벽을 세운 개수, pre : 이전에 벽을 세운 곳
def dfs(cnt, pre):
    global max_v
    if cnt == 3:    # 벽을 최대 3개 세울 수 있으므로 cnt가 3이 되면 계산
        result = 0  # 바이러스가 퍼진 곳 개수
        # visited : 바이러스가 퍼진 곳 저장, 퍼진 곳에 다시 퍼지면 안됨
        visited = [[0]*M for _ in range(N)]
        for y in range(N):
            for x in range(M):
                if arr[y][x] == 2: # 바이러스가 있는 곳 부터 bfs로 퍼뜨릴 수 있는 곳 개수 계산
                    result += bfs(y, x, visited)
        sum_v = 0   # 벽을 제외한 모든 칸 개수
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 1:
                    sum_v += 1
        result = sum_v-result       # 안전지대의 개수 = 벽을 제외한 칸의 개수 - 바이러스가 퍼진 칸 개수
        max_v = max(max_v, result)  # 안전지대 개수 최대값 저장
        return  # 탐색 종료
    for idx in range(pre+1, N*M):   # 이전에 벽을 세운 곳 다음부터 세우기
        i, j = idx//M, idx%M        # 1차원 인덱스 기준으로 2차원 좌표 계산
        if arr[i][j]: # 칸이 1 또는 2일 때(벽을 세울 수 없을 때) 넘어가기
            continue
        arr[i][j] = 1
        dfs(cnt+1, idx)
        arr[i][j] = 0

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_v = 0   # 안전지대의 최대값
dfs(0, -1)  # dfs로 3개의 벽을 세우는 모든 경우를 계산
print(max_v)