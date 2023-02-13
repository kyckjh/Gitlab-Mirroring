import sys
sys.stdin = open("input.txt", "r")

def hm(N, M, arr):
    result = 0
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
                result += 1
            k = 0
            while k < M//2:
                if arr[j+k][i] == arr[j+M-k-1][i]:
                    k += 1
                    continue
                else:
                    break
            if k == M//2:
                result += 1
    return result


for t in range(1, 11):
    n = int(input())
    arr = [input() for _ in range(8)]
    result = hm(8, n, arr)
    print(f'#{t} {result}')

