import sys
N, S = map(int, sys.stdin.readline().split())

selected = [0] * N
K = 3
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
def comb(idx, S):
    global ans

    if idx == N:
        sum = 0
        for i in range(N):
            if selected[i]:
                sum += arr[i]
        if sum == S:
            ans += 1
            return
        else:
            return

    for i in range(1, -1, -1):
        selected[idx] = i
        comb(idx + 1, S)

comb(0, S)
if S == 0:
    print(ans-1)
else:
    print(ans)


# def summ(N, S):
#     result = [[0]*N for _ in range(N)]
#     ans = 0
#     for i in range(0, N):
#         result[i][i] = arr[i]
#         if result[i][i] == S:
#             ans += 1
#
#     for k in range(1, N):
#         for i in range(0, N-k):
#             result[i][i+k] = result[i][i+k - 1] + result[i+k][i+k]
#             if result[i][i+k] == S:
#                 ans += 1
#     return ans