import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort()
for i in range(N):
    arr[i] = arr[i][1]
max_v = 1
dp = [0]*N
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
            if max_v < dp[i]:
                max_v = dp[i]
print(N-max_v)