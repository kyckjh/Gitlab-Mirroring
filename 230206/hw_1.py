def bit_count(num):
    bi = []
    cnt = 0
    while num > 0:
        if num%2:
            bi.append(1)
            cnt += 1
        else:
            bi.append(0)
        num //= 2
    return bi, cnt
#print(bit_count(5))
T = int(input())
A = list(range(1, 13))
#print(A)
# for t in range(1, T+1):
#     N, K = map(int, input().split())
#     bit = 1<<N
#     result = 0
#     for i in range(1<<12):
#         bi, cnt = bit_count(i)
#         if cnt == N:
#             #print(bi, cnt)
#             sum = 0
#             for j in range(len(bi)):
#                 sum += A[j] * bi[j]
#             if sum == K:
#                 result += 1
#     print(f'#{t} {result}')
        
bit = 0
def test(N, bit, arr, K):
    if N == 0:
        sum = 0
        for k in range(12):
            if bit & (1 << k):
                print(type(sum), sum)
                print(arr)
                sum += arr[k]
        if sum == K:
            return 1
        else:
            return 0
    sum = 0
    for i in range(N+1, 12-N):
        bit += 1 << i
        sum += test(i, bit, A, K)
        bit -= 1 << i
    return sum

for t in range(1, T+1):
    N, K = map(int, input().split())
    bit = 1<<N
    result = 0
    for i in range(13-N):
        result += test(i, 0, A, K)  #  깊이 추가 필요
    print(f'#{t} {result}')