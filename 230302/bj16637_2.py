import sys

def f(lst):
    global max_v
    if len(lst) == 3:
        r = 0
        if lst[1] == '+':
            r = lst[0] + lst[2]
        elif lst[1] == '-':
            r = lst[0] - lst[2]
        else:
            r = lst[0] * lst[2]
        if r > max_v:
            max_v = r
        return
    elif len(lst) == 1:
        if lst[0] > max_v:
            max_v = lst[0]
        return
    temp = 0
    if lst[1] == '+':
        temp = lst[0] + lst[2]
    elif lst[1] == '-':
        temp = lst[0] - lst[2]
    else:
        temp = lst[0] * lst[2]
    f([temp]+lst[3:])
    temp = 0
    if lst[3] == '+':
        temp = lst[2] + lst[4]
    elif lst[3] == '-':
        temp = lst[2] - lst[4]
    else:
        temp = lst[2] * lst[4]
    if lst[1] == '+':
        temp = lst[0] + temp
    elif lst[1] == '-':
        temp = lst[0] - temp
    else:
        temp = lst[0] * temp
    f([temp]+lst[5:])

N = int(sys.stdin.readline())
arr = list(map(str, sys.stdin.readline().strip()))
for i in range(0, N, 2):
    arr[i] = int(arr[i])
max_v = -2**31
f(arr)
print(max_v)