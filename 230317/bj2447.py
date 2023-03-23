import sys
sys.setrecursionlimit(10**7)

def star(y, x, blank, n):
    if n == 3:
        if blank:
            for i in range(3):
                if i==1:
                    ans[y][x+i] = '***'
                else:
                    ans[y][x+i] = '* *'
        else:
            for i in range(3):
                ans[y][x+i] = '   '
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
        for i in range(3*n):
            for j in range(3*n):
                ans[y+i][x+j] = '   '

N = int(sys.stdin.readline())
N //= 9
ans = [['']*N for _ in range(N)]
ans2 = [' ']*N

# f(N)

star(0, 0, 1, N)


for i in range(3):
    if i == 1:
        for k in range(N):
            print("".join(ans[k]), end='')
            print("".join(ans2), end='')
            print("".join(ans[k]), end='')
            print()
    else:
        for k in range(N):
            for l in range(3):
                print("".join(ans[k]), end='')
            print()