import sys
sys.stdin = open("input.txt", "r")

lst = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    idx = 0
    for i in range(N):
        if '1' in arr[i]:
            idx = i
            break
    last = M
    for i in range(M-1, -1, -1):
        if arr[idx][i] == '1':
            last = i
            break
    check = []
    for i in range(last, last-8*7, -7):
        code = 0
        for j in range(0, 7):
            code += int(arr[idx][i-j])*pow(2, j)
        check.append(lst.index(code))
    ans = 0
    for i in range(len(check)):
        if i%2:
            ans += check[i]*3
        else:
            ans += check[i]
    if ans%10:
        print(f'#{t} 0')
    else:
        print(f'#{t} {sum(check)}')
