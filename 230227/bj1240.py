import sys
N, M = map(int, sys.stdin.readline().split())
node_dict = {}

def dis(a, b):
    queue = []
    visited = [0]*1001
    for way in node_dict[a]:
        queue.append(way)
        visited[way[0]] = 1
    while queue:
        next, distance = queue.pop(0)
        if next == b:
            return distance
        for way in node_dict[next]:
            if visited[way[0]] == 0:
                visited[way[0]] = 1
                queue.append((way[0], way[1]+distance))

for _ in range(N-1):
    a, b, d = map(int, sys.stdin.readline().split())
    node_dict.setdefault(a, [])
    node_dict[a].append((b, d))
    node_dict.setdefault(b, [])
    node_dict[b].append((a, d))
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dis(a, b))

'''
5 1
1 2 1
2 3 1
3 4 10
3 5 1
1 5
'''