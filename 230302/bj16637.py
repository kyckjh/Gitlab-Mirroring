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

    for i in range(1, len(lst), 2):
        temp_lst = lst[:]
        temp = 0
        if lst[i] == '+':
            temp = lst[i-1] + lst[i+1]
        elif lst[i] == '-':
            temp = lst[i-1] - lst[i+1]
        else:
            temp = lst[i-1] * lst[i+1]
        temp_lst.pop(i-1)
        temp_lst.pop(i-1)
        temp_lst[i-1] = temp
        f(temp_lst)

N = int(sys.stdin.readline())
arr = list(map(str, sys.stdin.readline().strip()))
for i in range(0, N, 2):
    arr[i] = int(arr[i])
max_v = 0
f(arr)
print(max_v)