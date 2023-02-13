import sys
sys.stdin = open("sample_input(1).txt", "r")

dir = [(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,1),(1,-1),(-1,-1)]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    Nm = N - 1
    board[Nm // 2][Nm // 2] = 2
    board[Nm // 2][Nm // 2 + 1] = 1
    board[Nm // 2 + 1][Nm // 2] = 1
    board[Nm // 2 + 1][Nm // 2 + 1] = 2

    for m in range(M):
        j, i, bw = map(int, input().split())
        i, j = i-1, j-1
        board[i][j] = bw
        for dr in dir:
            ci, cj = i, j
            ci += dr[0]
            cj += dr[1]
            while 0 <= ci < N and 0 <= cj < N:
                if board[ci][cj] == 0:
                    break
                elif board[ci][cj] == bw:
                    cnt = (ci - i) * dr[0] + (cj - j) * dr[1]
                    if i != ci and j != cj:
                        cnt //= 2
                    for k in range(cnt):
                        board[i + k * dr[0]][j + k * dr[1]] = bw
                    break
                ci += dr[0]
                cj += dr[1]
    sum1 = 0
    sum2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sum1 += 1
            elif board[i][j] == 2:
                sum2 += 1
    print(f'#{t} {sum1} {sum2}')
