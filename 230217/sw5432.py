# import sys
# sys.stdin = open("input1.txt", "r")

T = int(input())
for t in range(1, T+1):
    s = input()
    ans = cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt+=1
        else:
            if s[i-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1
    print(f'#{t} {ans}')