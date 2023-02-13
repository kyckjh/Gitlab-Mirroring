import sys
sys.stdin = open("input2.txt", "r")

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
                return True
            k = 0
            while k < M//2:
                if arr[j+k][i] == arr[j+M-k-1][i]:
                    k += 1
                    continue
                else:
                    break
            if k == M//2:
                return True
    return False


for _ in range(10):
    t = input()
    arr = [input() for _ in range(100)]
    maxResult = 0
    for i in range(1, 101):
        result = hm(100, i, arr)
        if result:
            maxResult = i
    print(f'#{t} {maxResult}')

