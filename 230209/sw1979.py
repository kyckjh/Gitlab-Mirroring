import sys
sys.stdin = open("input3.txt", "r")
'''
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        num1_1 = 0
        num1_2 = 0
        for j in range(N):
            if arr[i][j] == 1:
                num1_1 += 1
            else:
                if num1_1 == K:
                    result += 1
                num1_1 = 0
            if arr[j][i] == 1:
                num1_2 += 1
            else:
                if num1_2 == K:
                    result += 1
                num1_2 = 0
        else:
            if num1_1 == K:
                result += 1
            if num1_2 == K:
                result += 1
    print(f'#{t} {result}')
'''
def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    arr_t = list(map(list, zip(*arr)))
    ans = count(arr) + count(arr_t)
    print(f'#{t} {ans}')