st = input()

stack = []
ans = []
for char in st:
    if char == '(':
        stack.append(char)
        continue
    if char in ['+', '-']:
        while stack and stack[-1] != '(':
            ans.append(stack.pop())
        stack.append(char)
    elif char in ['*', '/']:
        while stack and stack[-1] in ['*', '/']:
            ans.append(stack.pop())
        stack.append(char)
    elif char == ')':
        while stack[-1] != '(':
            ans.append(stack.pop())
        stack.pop()
    else:   # 숫자일때
        ans.append(char)

while stack:
    ans.append(stack.pop())

print("".join(ans))