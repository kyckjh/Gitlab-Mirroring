import sys
sys.stdin = open("sample_input2.txt", "r")

ways = [[], [(0, 1), (1, 0), (0, -1), (-1, 0)], [(1, 0), (-1, 0)], [(0, 1), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]]

def bfs(i, j):
    queue = []
    cnt = 1
    time = 0
    queue.append((i, j, time))
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    while queue:
        ci, cj, time = queue.pop(0)
        if time > L-2:
            continue
        for y, x in ways[arr[ci][cj]]:
            ni, nj = ci + y, cj + x
            # 나갈 수 있는 방향이면
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                # 들어갈 수 있는 방향이면
                if (-y, -x) in ways[arr[ni][nj]]:
                    cnt += 1
                    visited[ni][nj] = 1
                    queue.append((ni, nj, time + 1))
    return cnt

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(R, C)
    print(f'#{t} {ans}')