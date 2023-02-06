import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    T = int(input())    
    sum_r = 0
    sum_c = [0]*100
    sum_d1 = 0
    sum_d2 = 0    
    for i in range(100):
        temp_row = list(map(int, input().split()))
        temp_max_r = 0
        for j in range(100):
            sum_c[j] += temp_row[j]
            temp_max_r += temp_row[j]
            if i == j:
                sum_d1 += temp_row[j]
            if i == 99-j:
                sum_d2 += temp_row[j]
        if temp_max_r > sum_r:
            sum_r = temp_max_r    
    sum_c.extend([sum_r, sum_d1, sum_d2])
    result = 0
    for max_sum in sum_c:
        if result < max_sum:
            result = max_sum
    print(f'#{t} {result}')