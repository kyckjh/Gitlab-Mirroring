import sys

sys.stdin = open("input.txt", "r")


def bfs(s):
    q = []
    v = [0] * 101
    ans = s

    q.append(s)
    v[s] = 1
    while q:
        c = q.pop(0)
        if v[ans] < v[c] or v[ans] == v[c] and ans < c:
            ans = c

        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
    return ans


T = 10
for t in range(1, T + 1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        s, e = lst[i], lst[i + 1]
        adj[s].append(e)
    ans = bfs(S)
    print(f'#{t} {ans}')
