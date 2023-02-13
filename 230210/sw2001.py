import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxSum = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            tempSum = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    tempSum += arr[x][y]
            if maxSum < tempSum:
                maxSum = tempSum
    print(f'#{t} {maxSum}')