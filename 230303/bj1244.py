import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for _ in range(M):
    gen, num = map(int, sys.stdin.readline().split())
    if gen == 1:
        for i in range(num-1, N, num):
            arr[i] = abs(arr[i]-1)
    else:
        cnt = 1
        num -= 1
        while 0<=num-cnt and num+cnt<N:
            if arr[num-cnt] != arr[num+cnt]:
                break
            cnt += 1
        cnt -= 1
        for j in range(num-cnt, num+cnt+1):
            arr[j] = abs(arr[j]-1)
print(arr[0], end=' ')
for i in range(1, N):
    if i % 20 == 0:
        print()
    print(arr[i], end=' ')

'''
30
1 0 1 0 0 0 1 1 0 0 1 0 1 0 0 0 1 1 0 0 1 0 1 0 0 0 1 1 0 0 
2
1 3
2 3

'''