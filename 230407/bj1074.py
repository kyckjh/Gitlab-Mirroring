import sys

def f(N, r, c):
    if N < 0:
        return 0
    result = 0
    if r >= 2**N:
        result += 4**N*2
        r -= 2**N
    if c >= 2**N:
        result += 4**N
        c -= 2**N
    result += f(N-1, r, c)
    return result

N, r, c = map(int, sys.stdin.readline().split())
result = f(N-1, r, c)
print (result)