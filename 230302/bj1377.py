import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
last = arr[-1]
ans = 1
for i in range(N-2, -1, -1):
    if arr[i] > last:
        ans += 1
    else:
        last = arr[i]
print(ans)
