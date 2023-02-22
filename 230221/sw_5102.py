import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    queue = []
    for _ in range(E):
        s, g = map(int, input().split())
        adj[s].append(g)
        adj[g].append(s)
    S, G = map(int, input().split())
    result = 0
    queue.append((S, 0))
    while queue:
        cnode, depth = queue.pop(0)
        if cnode == G:
            result = depth
            break
        depth += 1
        for node in adj[cnode]:
            if not visited[node]:
                queue.append((node, depth))
                visited[node] = 1
    print(f'#{t} {result}')