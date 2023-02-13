import sys
sys.stdin = open("sample_input.txt", "r")

def hm(N, M, arr):
    for i in range(N):
        for j in range(N-M+1):
            k = 0
            while k < M//2:
                if arr[i][j+k] == arr[i][j+M-k-1]:
                    k += 1
                    continue
                else:
                    break
            if k == M//2:
                return i, j, True
            k = 0
            while k < M//2:
                if arr[j+k][i] == arr[j+M-k-1][i]:
                    k += 1
                    continue
                else:
                    break
            if k == M//2:
                return i, j, False
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    resulti, resultj, isRow = hm(N, M, arr)
    print(f'#{t}', end=' ')
    if isRow:
        print(arr[resulti][resultj:resultj+M])
    else:
        for i in range(M):
            print(arr[resultj + i][resulti], end='')
        print()
