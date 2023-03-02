import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr1 = list(set(arr))
arr1.sort()
arr_dict = dict()
for idx, n in enumerate(arr1):
    arr_dict[n] = idx
for i in range(len(arr)):
    arr[i] = arr_dict[arr[i]]
print(*arr)

