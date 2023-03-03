T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    print(f'#{t}', end=' ')
    for time in arr:
        cnt += 1
        if time//M*K < cnt:
            print('Impossible')
            break
    else:
        print('Possible')
