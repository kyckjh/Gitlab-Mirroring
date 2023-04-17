import sys
input = sys.stdin.readline
TC = int(input())

def f(n):
    pass

for _ in range(TC):
    N, M, W = map(int, input().split())
    lst = [[] for _ in range(N)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        lst[S].append((T, E))
        lst[E].append((T, S))
    for _ in range(W):
        S, E, T = map(int, input().split())
        lst[S].append((T, E))
    dis = [float("inf")]*(N+1)
    for i in range(N):
        f(i)