import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())
cnt = 0
i = 0
while cnt < S and cnt < N and i < N:
    max_v = max(arr[i:S + 1])
    max_idx = arr.index(max_v)
    if max_idx == i:
        i += 1
        continue
    i += 1
    arr.pop(max_idx)
    arr.insert(cnt, max_v)
    cnt += 1
    S -= max_idx - cnt
print(arr)

'''
20
1 1 1 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 3
10
'''