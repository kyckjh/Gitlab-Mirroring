import sys
input = sys.stdin.readline

N = int(input())
cross = [0]*(N+1)
arr = []
for i in range(N):
    s, e = map(int, input().split())
    for num, line in enumerate(arr):
        ts, te = line
        if (s-ts)*(e-te)<0:
            cross[num] += 1
            cross[i] += 1
    arr.append([s, e])
ans = 0
for i in range(N):
    arr[i] = arr[i]+[cross[i]]
arr.sort()
print(arr)
print(cross)
for i in range(N):
    cross[i] = arr[i][2]
    arr[i] = [arr[i][0], arr[i][1]]
print(arr)
print(cross)
while cross.count(0) < N+1:
    print(cross)
    ans += 1
    pre_v = cross[0]
    max_idx = 0
    pre_idx = 0
    pre_cnt = 0
    max_cnt = 0
    for i in range(N+1):
        if pre_v > cross[i]:
            if max_cnt < pre_cnt:
                max_cnt = pre_cnt
                max_idx = i
            pre_cnt = 0
            continue
        pre_cnt += 1
        pre_v = cross[i]
        pre_idx = i
    s, e = arr[max_idx]
    for num, line in enumerate(arr):
        ts, te = line
        if (s - ts) * (e - te) < 0:
            if cross[num] > 0:
                cross[num] -= 1
    cross[max_idx] = 0
    print(pre_idx)
    print(max_idx)
print(ans)

'''
5
1 3
3 1
2 5
4 6
6 4

ans : 2
'''