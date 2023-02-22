import sys
N = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
root = 0
for i in range(0, N):
    if inputs[i] == -1:
        root = i
    else:
        adj[inputs[i]].append(i)
adj[delete_node].clear()
for i in range(N+1):
    if delete_node in adj[i]:
        adj[i].remove(delete_node)
ans = 0
queue = [root]
while queue:
    cnode = queue.pop(0)
    if cnode == delete_node:
        continue
    if adj[cnode] == []:
        ans += 1
        continue
    for node in adj[cnode]:
        queue.append(node)

print(ans)