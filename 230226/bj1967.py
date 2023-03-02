import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
childs = []
visited = [0]*(N+1)
max_result = 0
def search(i):
    global max_result
    visited[i] = 1
    max_v = 0
    temp_sum = []
    for child, dis in childs[i]:
        if visited[child] == 0:
            temp = search(child) + dis
            temp_sum.append(temp)
            if max_v < temp:
                max_v = temp
    if len(temp_sum) > 1:
        temp_sum.sort(reverse=True)
        tsum = temp_sum[0]+temp_sum[1]
        if max_result < tsum:
            max_result = tsum
    return max_v

for _ in range(N+1):
    childs.append([])
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    a = arr[0]
    for i in range(1, len(arr)-1, 2):
        b, c = arr[i], arr[i+1]
        childs[a].append((b, c))
temp_max = search(1)
if max_result < temp_max:
    max_result = temp_max
print(max_result)

'''
5
1 2 3
1 3 4
1 4 5
1 5 6
'''