import sys
sys.stdin = open("input2.txt", "r")

def bfs(n):
    queue = []
    result = {}
    cnt = 0
    queue.append((n, cnt))
    visited = [0]*101
    visited[n] = 1
    while queue:
        now, cnt = queue.pop(0)
        if call_v[now] == []:
            continue
        for next in call_v[now]:
            if not visited[next]:
                visited[next] = 1
                queue.append((next, cnt+1))
                result.setdefault(cnt+1, [])
                result[cnt+1].append(next)
    return max(result[cnt])

for t in range(1, 11):
    N, start = map(int, input().split())
    data = list(map(int, input().split()))
    call_v = []
    for _ in range(101):
        call_v.append([])
    for i in range(0, N, 2):
        call_v[data[i]].append(data[i + 1])
    ans = bfs(start)
    print(f'#{t} {ans}')

