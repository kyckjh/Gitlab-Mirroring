import sys
input = sys.stdin.readline

def check(x, y):
    lst = [1]*10
    for num in arr[y]:
        lst[num] = 0
    arr2 = list(zip(*arr))
    for num in arr2[x]:
        lst[num] = 0
    x = (x//3)*3
    y = (y//3)*3
    for i in range(y, y+3):
        for j in range(x, x+3):
            lst[arr[i][j]] = 0
    result = []
    for i in range(1, 10):
        if lst[i]:
            result.append(i)
    return result

def dfs(i, k):
    if i == k-1:
        print('<<<<<<<<<<<<<')
        for i in range(9):
            print(*arr[i])
        return

    y, x = zeros.pop()
    lst = check(y, x)
    if not lst:
        print(y, x, i)
    while lst:
        num = lst.pop()
        arr[y][x] = num
        dfs(i+1, k)
    arr[y][x] = 0
    zeros.append((y, x))
    return

arr = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            zeros.append((i, j))

dfs(0, len(zeros)-1)

