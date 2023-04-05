import sys
sys.stdin = open("sample_input.txt", "r")

# 우선순위큐 push
def push(queue, key_idx, value):
    global queue_size
    queue[queue_size] = value
    queue_size += 1
    idx = queue_size-1
    while idx != 1:
        if queue[idx//2][key_idx] > queue[idx][key_idx]:
            queue[idx // 2], queue[idx] = queue[idx], queue[idx // 2]
            idx //= 2
        else:
            break

# 우선순위큐 pop
def pop(queue, key_idx):
    global queue_size
    parent = 1
    result = queue[1]
    queue[1] = queue[queue_size-1]
    queue_size -= 1
    child = parent*2
    while child < queue_size:
        if child+1 < queue_size:
            if queue[child][key_idx] > queue[child+1][key_idx]:
                child += 1
        if queue[child][key_idx] < queue[parent][key_idx]:
            queue[child], queue[parent] = queue[parent], queue[child]
            parent = child
            child = parent*2
        else:
            break
    return result
'''
T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    queue = []
    mst = set()
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    push(queue, 1, (0, 0))
    result = 0
    while len(mst) < V+1:
        v, w = pop(queue, 1)
        if v in mst:
            continue
        mst.add(v)
        result += w
        for i in range(V+1):
            if i not in mst and adj[v][i]:
                push(queue, 1, (i, adj[v][i]))
    print(f'#{t} {result}')
'''


def find_set(x):
    if p[x] == x:
        return x
    p[x] = p[find_set(p[x])]
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    p = [x for x in range(V + 1)]
    queue = [0]*(V+E+1)
    queue_size = 1
    result = 0
    graph = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph.append((n1, n2, w))
    for i in range(E):
        push(queue, 2, graph[i])
    while queue_size > 1:
        n1, n2, weight = pop(queue, 2)
        if find_set(n1) == find_set(n2):
            continue
        union(n1, n2)
        result += weight
    print(f'#{t} {result}')


