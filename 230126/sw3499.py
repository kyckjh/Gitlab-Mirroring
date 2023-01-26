T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(input().split())
    result = []
    if N % 2:   # N이 홀수일 때
        for i in range(N // 2):
            result.append(arr[i])
            result.append(arr[i + N // 2 + 1])
        result.append(arr[N // 2])
    else:   # 짝수일 때
        for i in range(N // 2):
            result.append(arr[i])
            result.append(arr[i + N // 2])
    print(f'#{test_case}', *result)
    
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(input().split())
#     print(f'#{test_case}', end=' ')
#     if N % 2:   # N이 홀수일 때
#         for i in range(N // 2):
#             print(arr[i], end=' ')
#             print(arr[i + N // 2 + 1], end=' ')
#         print(arr[N // 2], end=' ')
#     else:   # 짝수일 때
#         for i in range(N // 2):
#             print(arr[i], end=' ')
#             print(arr[i + N // 2], end=' ')
#     print()