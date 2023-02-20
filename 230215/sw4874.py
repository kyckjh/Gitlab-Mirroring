T = int(input())
for t in range(1, T+1):
    arr = list(map(str, input().split()))
    stack = []
    result = 0
    for s in arr:
        if s in ['+', '-', '*', '/']:
            if len(stack) > 1:
                b, a = int(stack.pop()), int(stack.pop())
                if s == '+':
                    stack.append(a+b)
                elif s == '-':
                    stack.append(a-b)
                elif s == '*':
                    stack.append(a*b)
                else:
                    stack.append(a//b)
            else:
                result = 'error'
                break
        else:
            if s == '.':
                if len(stack) == 1:
                    result = stack[0]
                else:
                    result = 'error'
            else:
                stack.append(s)

    print(f'#{t} {result}')

