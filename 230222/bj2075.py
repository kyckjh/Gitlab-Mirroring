import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
idx_lst = [N-1]*N
result = 0
for _ in range(N):
    max_idx = 0
    max_v = -1000000001
    for i in range(N):
        if max_v < arr[idx_lst[i]][i]:
            max_v = arr[idx_lst[i]][i]
            max_idx = i
    idx_lst[max_idx] -= 1
    result = max_v
print(result)
