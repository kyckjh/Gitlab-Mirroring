import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    half = N // 2
    lst = []
    cnt = 1
    while half >= 0:
        temp_lst = []
        for i in range(half, half + cnt):
            temp_lst.append(i)
        half -= 1
        cnt += 2
        lst.append(temp_lst)
    for value in lst[-2::-1]:
        lst.append(value)
    arr = []
    for i in range(N):
        temp_arr = []
        for j in map(int, input()):
            temp_arr.append(j)
        arr.append(temp_arr)
    result = 0
    for idx, row in enumerate(lst):
        for column in row:
            result += arr[idx][column] 
    print(f'#{t}',result)