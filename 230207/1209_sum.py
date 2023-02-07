T = 10
for _ in range(T):
    t = int(input())
    result = -0xffffffff
    board = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += board[i][j]
        if sum_row > result:
            result = sum_row

    for i in range(100):
        sum_col = 0
        for j in range(100):
            sum_col += board[j][i]
        if sum_col > result:
            result = sum_col

    sum_dia1 = 0
    sum_dia2 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum_dia1 += board[i][j]
            if i + j == 99:
                sum_dia2 += board[i][j]

    result = result if result > sum_dia1 else sum_dia1
    result = result if result > sum_dia2 else sum_dia2

    print(f'#{t} {result}')
