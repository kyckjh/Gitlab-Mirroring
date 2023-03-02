import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
parents = [-1]*(N+1)
childs = []
visited = [0]*(N+1)
def search(i):
    if visited[i] == 1:
        return False
    visited[i] = 1
    for n in childs[i]:
        if search(n):
            parents[n] = i
    return True

for _ in range(N+1):
    childs.append([])
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    childs[a].append(b)
    childs[b].append(a)
search(1)
for k in range(2, N+1):
    print(parents[k])