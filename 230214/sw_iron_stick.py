T = int(input())
for t in range(1, T+1):
    s = input()
    stack = [s[0]]
    result = 0
    for i in range(1, len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            stack.pop()
            result += 1 if s[i-1] == ')' else len(stack)
    print(f'#{t} {result}')

'''
2
()(((()())(())()))(())
(((()(()()))(())()))(()())
'''