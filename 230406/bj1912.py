import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans = -0xffffffff
temp_sum = 0
for i in range(N):
    temp_sum += arr[i]
    ans = max(ans, temp_sum)
    if temp_sum < 0:
        temp_sum = 0
print(ans)