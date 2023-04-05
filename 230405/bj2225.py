import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1

for j in range(1, K+1):
    temp = 0
    for i in range(0, N+1):
        temp += dp[i][j-1]
        dp[i][j] += temp

print(dp[N][K]%1000000000)
