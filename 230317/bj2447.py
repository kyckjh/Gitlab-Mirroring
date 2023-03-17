import sys
sys.setrecursionlimit(10**9)

stars = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
blanks = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def star(y, x, blank, n):
    if n == 3:
        if blank:
            ans[y//3][x//3] = stars
            # for i in range(3):
            #     for j in range(3):
            #         if i==1 and j==1:
            #             ans[y+i][x+j] = False
            #         else:
            #             ans[y+i][x+j] = True
        else:
            ans[y//3][x//3] = blanks
            # for i in range(3):
            #     for j in range(3):
            #         ans[y+i][x+j] = False
        return
    n //= 3
    if blank:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    star(y + n*i, x + n*j, 0, n)
                else:
                    star(y + n*i, x + n*j, 1, n)
    else:
        for i in range(3):
            for j in range(3):
                star(y + n*i, x + n*j, 0, n)

N = int(sys.stdin.readline())
N //= 3
ans = [[0]*N for _ in range(N)]
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            star(N*i, N*j, 0, N)
        else:
            star(N*i, N*j, 1, N)

for i in range(N):
    result = [[], [], []]
    for j in range(N):
        for a in range(3):
            result[a].append(ans[i][j][a])
    for j in range(3):
        for k in range(3):
            print("".join(result[j][k]), end='')
    print()