import sys
input = sys.stdin.readline
N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
arr2 = []
for i in range(1, N):
    arr2.append(arr[i]-arr[i-1])
arr2.sort()
print(arr2)
print(arr2[C])