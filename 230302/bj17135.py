def distance(r1, c1, r2, c2):
    return abs(r1-r2)+abs(c1-c2)

def game(a, b, c, lst):
    result = 0
    archers = [(N, a), (N, b), (N, c)]
    while lst:
        idxs = set()
        for j in range(len(archers)):
            min_d = N+M+1
            idx = -1
            for i in range(len(lst)):
                d = distance(lst[i][0], lst[i][1], archers[j][0], archers[j][1])
                if d <= D:
                    if d < min_d:
                        min_d = d
                        idx = i
                    if d == min_d:
                        if lst[i][1] < lst[idx][1]:
                            idx = i
            if idx != -1:
                idxs.add(idx)
        result += len(idxs)
        idxs = list(idxs)
        idxs.sort()
        for i in range(len(idxs)-1, -1, -1):
            lst.pop(idxs[i])
        for i in range(len(lst)):
            lst[i][0] += 1
        for i in range(len(lst)-1, -1, -1):
            if lst[i][0] >= N:
                lst.pop(i)
    return result

import sys
import copy

N, M, D = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
enemies = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enemies.append([i, j])
arc = [0]*M
max_v = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            result = game(i, j, k, copy.deepcopy(enemies))
            if result > max_v:
                max_v = result
print(max_v)
