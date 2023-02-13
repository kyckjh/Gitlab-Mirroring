T = int(input())
for t in range(1, T+1):
    s = input()
    result = 0
    nums = 0
    for i in range(1, len(s)):
        if s[i] == '(':
            if s[i-1] == '(':
                nums += 1
            else:
                continue
        else:
            if s[i-1] == '(':
                result += nums
            else:
                nums -= 1
                result += 1
    print(f'#{t} {result}')

'''
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
'''

'''
T = int(input())
for t in range(1, T+1):
    s = input() + ' '
    result = 0
    nums = 0
    i = 1
    while i < len(s) - 1:
        if s[i] == '(':
            if s[i-1] == '(':
                while s[i+1] == '(':
                    nums += 1
                    i += 1
                nums += 1
                i += 1
            else:
                i += 1
                continue
        else:
            if s[i-1] == '(':
                result += nums
                i += 1
            else:
                while s[i+1] == ')':
                    i += 1
                    nums -= 1
                    result += 1
                i += 1
                nums -= 1
                result += 1
    print(f'#{t} {result}')
'''

