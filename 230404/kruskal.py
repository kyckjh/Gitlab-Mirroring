'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

V, E = map(int, input().split())
graph = []
mst = set()
# 사이클이 생기는 걸 확인하기 위해 서로소 집합 활용
p = [x for x in range(V+1)]
def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

for _ in range(E):
    a, b, weight = map(int, input().split())
    graph.append((a,b,weight))
graph.sort(key=lambda x:x[2])
print(graph)
for i in range(E):
    # 작은거 선택해서 mst에 넣기
    if find_set(graph[i][0]) == find_set(graph[i][1]):
        continue
    mst.add(graph[i])
    union(graph[i][0], graph[i][1])