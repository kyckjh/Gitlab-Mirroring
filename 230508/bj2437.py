import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
if arr[0] != 1:
    print(1)
    quit()
sum_v = 1
i = 0
while i < N-1 and sum_v+1 >= arr[i+1]:
    i += 1
    sum_v += arr[i]
print(sum_v+1)