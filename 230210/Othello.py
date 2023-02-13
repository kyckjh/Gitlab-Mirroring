import sys
sys.stdin = open("sample_input(1).txt", "r")

dir = [(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,1),(1,-1),(-1,-1)]

class Board:
    def __init__(self, N):
        self.N = N
        self.board = [[0] * N for _ in range(N)]
        self.board[(N-1) // 2][(N-1) // 2] = 2
        self.board[(N-1) // 2][(N-1) // 2 + 1] = 1
        self.board[(N-1) // 2 + 1][(N-1) // 2] = 1
        self.board[(N-1) // 2 + 1][(N-1) // 2 + 1] = 2

    def set_board(self, i, j, bw):
        self.board[i][j] = bw
        for dr in dir:
            ci, cj = i, j
            ci += dr[0]
            cj += dr[1]
            while 0 <= ci < N and 0 <= cj < N:
                if self.board[ci][cj] == 0:
                    break
                elif self.board[ci][cj] == bw:
                    if i == ci or j == cj:
                        for k in range((ci - i)*dr[0] + (cj-j)*dr[1]):
                            self.board[i + k*dr[0]][j + k*dr[1]] = bw
                        break
                    else:
                        for k in range((ci-i)*dr[0]):
                            self.board[i + k*dr[0]][j + k*dr[1]] = bw
                        break
                ci += dr[0]
                cj += dr[1]

    def get_board(self):
        sum1 = 0
        sum2 = 0
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 1:
                    sum1 += 1
                elif self.board[i][j] == 2:
                    sum2 += 1
        return sum1, sum2


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = Board(N)
    for m in range(M):
        j, i, bw = map(int, input().split())
        board.set_board(i-1, j-1, bw)
    sum1, sum2 = board.get_board()
    print(f'#{t} {sum1} {sum2}')
