import sys
input = sys.stdin.readline
TC = int(input())
INF = int(1e9)
def f():
    for n in range(N-1):
        for start, end, cost in lst:
            if dis[end] > dis[start]+cost:
                dis[end] = dis[start]+cost
    for start, end, cost in lst:
        if dis[end] > dis[start] + cost:
            return 'YES'
    return 'NO'

for _ in range(TC):
    N, M, W = map(int, input().split())
    lst = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        lst.append((S, E, T))
        lst.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        lst.append((S, E, -T))
    dis = [0]*(N+1)
    print(f())

'''
import sys
input = sys.stdin.readline
TC = int(input())
INF = int(1e9)
def f():
    for n in range(N-1):
        for i in range(1, N+1):
            cost, end = lst[i]
            if dis[end] > dis[i]+cost:
                dis[end] = dis[i]+cost
    for i in range(1, N + 1):
        cost, end = lst[i]
        if dis[end] > dis[i] + cost:
            return 'YES'
    return 'NO'

for _ in range(TC):
    N, M, W = map(int, input().split())
    lst = [False]*(N+1)
    for _ in range(M):
        S, E, T = map(int, input().split())
        if not lst[S]:
            lst[S] = (T, E)
        else:
            if lst[S][0] > T:
                lst[S] = (T, E)
        if not lst[E]:
            lst[E] = (T, S)
        else:
            if lst[E][0] > T:
                lst[E] = (T, S)
    for _ in range(W):
        S, E, T = map(int, input().split())
        lst[S] = (-T, E)
    dis = [0]*(N+1)
    print(lst)
    print(f())
'''
'''
1
4 3 1
1 2 3
2 3 3
3 4 3
2 4 7

'''