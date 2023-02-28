pq = {}

def su(i, p, q):
    if i == 0:
        return 1
    if i in pq:
        return pq[i]
    ans = su(i//p, p, q)+su(i//q, p, q)
    pq[i] = ans
    return ans

import sys
N, P, Q = map(int, sys.stdin.readline().split())
print(su(N, P, Q))