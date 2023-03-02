dirs = [(0,1), (1,1), (1,0)]
ff_dict = {}
def f(y, x, dir):
    if (y, x, dir) in ff_dict:
        return ff_dict[(y, x, dir)]
    result = 0
    if dir == 0:
        if y < 0 or y > N-1 or x+1 < 0 or x+1 > N-1 or arr[y][x+1] == 1:
            return 0
        if y == N-1 and x+1 == N-1:
            return 1
        result += f(y, x+1, 0)
        result += f(y, x+1, 1)
    elif dir == 2:
        if y+1 < 0 or y+1 > N-1 or x < 0 or x > N-1 or arr[y+1][x] == 1:
            return 0
        if y+1 == N-1 and x == N-1:
            return 1
        result += f(y+1, x, 1)
        result += f(y+1, x, 2)
    else:
        for r, c in dirs:
            nr, nc = y+r, x+c
            if nr < 0 or nr > N-1 or nc < 0 or nc > N-1 or arr[nr][nc] == 1:
                return 0
        if y+1 == N-1 and x+1 == N-1:
            return 1
        result += f(y+1, x+1, 0)
        result += f(y+1, x+1, 1)
        result += f(y+1, x+1, 2)
    ff_dict[(y, x, dir)] = result
    return result

import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = f(0, 0, 0)
print(ans)