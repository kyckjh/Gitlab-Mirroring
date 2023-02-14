'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
data = list(map(int, input().split()))
for i in range(0, E*2, 2):
    a, b = data[i], data[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
# for row in adj:
#     print(*row)
# dfs 시작
# 갈 수 있는 경로를 발견하면 이동하고,
# 길이 없으면 왔던 길을 되돌아감
# 되돌아가기 위해서 방문 경로를 저장
# stack을 이용해서 저장하면 편함
stack = []

# 재방문을 막기 위한 visited 배열 생성

def dfs(start):
    visited = [0] * (V+1)
    stack.append(start)
    visited[start] = 1
    print(start, end=' ')
    while stack:
        current = stack[-1]
        for i in range(1, V+1):
            if adj[current][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                print(i, end=' ')
                break
        else:
            stack.pop()

dfs(1)