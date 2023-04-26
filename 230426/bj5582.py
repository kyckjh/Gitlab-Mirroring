import sys
input = sys.stdin.readline


A = input().strip()
B = input().strip()
len_A = len(A)+1
len_B = len(B)+1

arr = [[0]*len_B for _ in range(len_A)]
for i in range(1, len_A):
    for j in range(1, len_B):
        if A[i-1] == B[j-1]:
            arr[i][j] = arr[i-1][j-1]+1
max_v = 0
for i in range(len_A):
    max_v = max(max_v, max(arr[i]))
print(max_v)