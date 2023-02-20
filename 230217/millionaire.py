T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    last = arr[-1]
    ans = temp = 0
    for i in range(N-2, -1, -1):
        if arr[i] < last:
            temp += last - arr[i]
        else:
            ans += temp
            last = arr[i]
            temp = 0
    print(f'#{t} {ans+temp}')

'''
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2'''