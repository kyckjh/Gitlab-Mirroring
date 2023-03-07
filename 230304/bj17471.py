import sys

def bfs(group, visited):
    node = group[0]
    result = 0
    visited[node] = 1
    queue = []
    for near in info[node]:
        queue.append(near)
    while queue:
        now = queue.pop(0)
        if visited[now] or now not in group:
            continue
        visited[now] = 1
        for next in info[now]:
            queue.append(next)

def comb(cnt, k):
    global min_v
    if cnt == k:
        a = []
        b = []
        for i in range(N):
            if select[i]:
                a.append(i)
            else:
                b.append(i)
        result1 = result2 = 0
        visited = [0]*N
        bfs(a, visited)
        for aa in a:
            if visited[aa] == 0:
                return
            result1 += population[aa]
        visited = [0]*N
        bfs(b, visited)
        for bb in b:
            if visited[bb] == 0:
                return
            result2 += population[bb]
        diff = abs(result1-result2)
        min_v = min(min_v, diff)
        return
    for i in range(N):
        if select[i]:
            continue
        select[i] = 1
        comb(cnt + 1, k)
        select[i] = 0


N = int(sys.stdin.readline())
population = list(map(int, sys.stdin.readline().split()))
info = []
min_v = float("inf")
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    info.append([])
    for j in range(a[0]):
        info[i].append(a[j+1]-1)
for i in range(1, N//2+1):
    select = [0]*N
    comb(0, i)
if min_v == float("inf"):
    print(-1)
else:
    print(min_v)