import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
min_v = min(arr)
max_v = max(arr)
first = 0
ans = 0
while first < N and arr[first] < 0:
    first += 1
i = 0

if first > 0:
    while i < first:
        ans -= arr[i]
        i += M
if first < N:
    i = N-1
    while i >= first:
        ans += arr[i]
        i -= M
ans *= 2
ans -= max_v if max_v > -min_v else -min_v
print(ans)
