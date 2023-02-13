import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxResult = 0
    for i in range(M):
        for j in range(N):
            result = arr[j][i]
            if i > 0:
                result += arr[j][i - 1]
            if i < M - 1:
                result += arr[j][i + 1]
            if j > 0:
                result += arr[j - 1][i]
            if j < N - 1:
                result += arr[j + 1][i]
            if result > maxResult:
                maxResult = result
    print(f'#{t} {maxResult}')