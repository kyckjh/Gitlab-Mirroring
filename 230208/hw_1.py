T = int(input())
for t in range(1, T+1):
    s = input()
    print(f'#{t} ', end='')
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            print(0)
            break
    else:
        print(1)