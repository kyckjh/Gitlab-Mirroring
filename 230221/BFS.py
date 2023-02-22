V, E = map(int, input().split())
adj_list = [[] for _ in range(V+1)]
data = list(map(int, input().split()))
for i in range(0, E*2, 2):
    adj_list[data[i]].append(data[i+1])
    adj_list[data[i+1]].append(data[i])

visited = [0]*(V+1)
queue = [1]
visited[1] = 1

while queue:
    front = queue.pop(0)
    print(front, end=' ')
    for node in adj_list[front]:
        if not visited[node]:
            queue.append((node))
            visited[node] = 1
print()
print('끝')

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''