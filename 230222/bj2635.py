def recur(n1, n2):
    if n1 < n2:
        return 1
    return 1 + recur(n2, n1-n2)

def recur2(n1, n2):
    print(n1, end=' ')
    if n2 < 0:
        return
    recur2(n2, n1-n2)

import sys
N = int(sys.stdin.readline())
max_v = 0
ans = 0
for i in range(1, N+1):
    result = recur(N, i)
    if max_v < result:
        ans = i
        max_v = result
print(max_v+1)
recur2(N, ans)