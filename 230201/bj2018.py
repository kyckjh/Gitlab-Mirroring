import time
start = time.time()  # 시작 시간 저장

def ss(n, k):
    sum_up = k*(k+1)//2
    if sum_up < n:
        return False, True
    k = k - n // k + 1
    diff = sum_up - n
    sum_down = k*(k+1)//2
    while sum_down >= diff:        
        if sum_down == diff:
            return True, False
        k -= 1
        sum_down = k*(k+1)//2
    return False, False

N = int(input())
cnt = 0
for i in range(N//2+1, 0, -1):
    result, k = ss(N, i)
    if result:
        cnt += 1
        if k:
            break
if N == 1 or N == 2:
    print(1)
else:
    print(cnt+1)


print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간




# def ss(n, k):
#     sum_up = k*(k+1)//2
#     k -= 1
#     while k > 0:
#         sum_down = k*(k-1)//2
#         if sum_up-sum_down == n:
#             return True, k
#         if sum_up-sum_down > n:
#             return False, k
#         k -= 1
#     return False, k

# N = int(input())
# cnt = 0
# for i in range(N//2+1, 0, -1):
#     result = False
#     result, k = ss(N, i)
#     if result:
#         cnt += 1
#         print(list(range(k, i+1)))
#         if k == 1:
#             break
#     elif (i*(i+1)//2) < N:
#         break
# print(cnt+1)