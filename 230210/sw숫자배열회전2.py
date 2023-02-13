import sys
sys.stdin = open("input_03.txt", "r")

import time

start = time.time()  # 시작 시간 저장

# 작업 코드


#import copy

def roll(arr):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = arr[N - j - 1][i]
    return result

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    result = []
    result.append(roll(arr))
    result.append(roll(result[0]))
    result.append(roll(result[1]))
    print(f'#{t}')
    for k in range(N):
        for r in range(3):
            print("".join(result[r][k]), end=' ')
        print()


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

# time : 0.003988981246948242
# time : 0.0009970664978027344