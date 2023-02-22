import sys
N = int(sys.stdin.readline())
A, B, C, D, E, F = map(int, sys.stdin.readline().split())
if N == 1:
    print(sum([A,B,C,D,E,F]) - max([A,B,C,D,E,F]))
else:
    arr = [A,B,C,F,E,D,A,B,C,F,E,D]
    one_min = min(arr)
    two_min = thr_min = 150
    for i in range(6):
        for j in range(i+1, i+6):
            if j == i+3:
                continue
            else:
                temp_sum = arr[i] + arr[j]
                if two_min > temp_sum:
                    two_min = temp_sum
    for i in range(6):
        for j in range(i+1, i+5):
            if j == i+3:
                continue
            for k in range(j+1, i+6):
                if k == i+3 or k == j+3:
                    continue
                else:
                    temp_sum = arr[i] + arr[j] + arr[k]
                    if thr_min > temp_sum:
                        thr_min = temp_sum
    result = (one_min * ((N-2)*(5*N-6)))+(two_min*(8*N-12))+(thr_min*4)
    print(result)