import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    _ = input()
    data = input()
    post = []
    stack = []
    for i in range(len(data)):
        if data[i] in '0123456789':
            post.append(data[i])
        else:
            if not stack:
                stack.append(data[i])
            else:
                post.append('+')
    post.append('+')

    stack = []
    for s in post:
        if s == '+':
            b, a = int(stack.pop()), int(stack.pop())
            stack.append(a+b)
        else:
            stack.append(s)

    print(f'#{t} {stack[0]}')

