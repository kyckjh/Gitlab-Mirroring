import sys
input = sys.stdin.readline

# i, j : 현재 칸의 좌표, cnt : 현재 칸에 쓰여있는 수
def dfs(i, j, cnt):
    if arr[i][j] == -1: # 도착점에 도달했으면
        print('HaruHaru')   # HaruHaru 출력 후 종료
        quit()
    for di, dj in [(1, 0), (0, 1)]: # 오른쪽과 아래 방향으로만 이동 가능
        ni, nj = di*cnt+i, dj*cnt+j # 현재 칸에 쓰여 있는 수 만큼 이동
        # 다음 이동할 칸이 범위 안에 있고 이동할 수 있는 칸의 수가 0이 아니고 아직 방문하지 않았으면 방문
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, arr[ni][nj])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dfs(0, 0, arr[0][0])    # 가장 왼쪽 위 칸에서 출발
print('Hing')   # 프로그램이 종료되지 않았으면 도착점에 도달하지 못했다는 뜻이므로 Hing 출력