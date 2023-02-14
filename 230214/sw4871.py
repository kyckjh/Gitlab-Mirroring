import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a][b] = 1
    S, G = map(int, input().split())
    stack = []
    visited = [0] * (V+1)
    start = S
    stack.append(start)
    result = 0
    while stack:
        current = stack[-1]
        if current == G:
            result = 1
            break
        visited[current] = 1
        for i in range(1, V+1):
            if adj[current][i] == 1 and visited[i] == 0:
                stack.append(i)
                print(i)
                break
        else:
            stack.pop()
    print(f'#{t} {result}')
