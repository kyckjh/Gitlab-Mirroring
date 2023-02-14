import sys
def summ(N, S):
    result = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(0, N):
        result[i][i] = arr[i]
        if result[i][i] == S:
            ans += 1

    for k in range(1, N):
        for i in range(0, N-k):
            result[i][i+k] = result[i][i+k - 1] + result[i+k][i+k]
            if result[i][i+k] == S:
                ans += 1
    return ans


N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = summ(N, S)
print(ans)