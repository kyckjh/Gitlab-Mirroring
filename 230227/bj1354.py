pq = {}

def su(i):
    if i <= 0:
        return 1
    if i in pq:
        return pq[i]
    ans = su(i//P-X)+su(i//Q-Y)
    pq[i] = ans
    return ans

import sys
sys.setrecursionlimit(10**9)
N, P, Q, X, Y = map(int, sys.stdin.readline().split())
print(su(N))