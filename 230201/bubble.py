'''
55 7 78 12 42
for i : 0 M-1 -> 1  # 각 구간의 끝
    for j : 0 -> i - 1  # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr [j] <-> arr[j+1]    # 큰 원소 오른쪽으로
'''
N = int(input())
arr = list(map(int, input().split()))
for i in range(N-1, 0, -1): # 각 구간의 끝
    for j in range(i):  # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j] # 큰 원소 오른쪽으로
print(arr)