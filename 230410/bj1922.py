import sys
input = sys.stdin.readline
V = int(input())
E = int(input())
graph = []
ans = 0
p = [x for x in range(V+1)]
def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

for _ in range(E):
    a, b, weight = map(int, input().split())
    graph.append((a,b,weight))
graph.sort(key=lambda x:x[2])
for i in range(E):
    if find_set(graph[i][0]) == find_set(graph[i][1]):
        continue
    ans += graph[i][2]
    union(graph[i][0], graph[i][1])

print(ans)