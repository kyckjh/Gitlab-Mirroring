import sys
sys.stdin = open("sample_input2.txt", "r")

def f(i, j, k, N): # i : 마지막 탐색한 곳, j : 현재탐색횟수, k : 목표탐색횟수, N : 배열 길이
    global minSum
    if j == k:
        temp_sum = 0
        wbr = 0
        for idx in range(N+2):
            if wbr == 0: # white로 칠할때
                temp_sum += arr[idx].count('B')
                temp_sum += arr[idx].count('R')
            elif wbr == 1: # blue
                temp_sum += arr[idx].count('W')
                temp_sum += arr[idx].count('R')
            else: # red
                temp_sum += arr[idx].count('W')
                temp_sum += arr[idx].count('B')
            if p[idx] == 1:
                wbr+=1
        #print(temp_sum)
        if minSum > temp_sum:
            minSum = temp_sum
        #print(p)
        return
    for l in range(i, N-k+j+2):
        p[l] = 1
        f(l+1, j+1, k, N)
        p[l] = 0

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    RBW = []
    ans = 0

    for lst in arr:
        red = lst.count('R')
        blue = lst.count('B')
        white = M - red - blue
        # 흰색으로 칠할때, 파란색으로 칠할때, 빨간색으로 칠할때
        RBW.append((red+blue, red+white, blue+white))
        #print(f'red: {red}, blue: {blue},white: {M - red - blue}')
    minSum = 100000000
    p = [0]*(N)
    f(0, 0, 2, N-2)

    print(f'#{t} {minSum}')