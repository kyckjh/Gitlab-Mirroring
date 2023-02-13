# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, num):
#         self.data.append(num)
#
#     def pop(self):
#         self.data.pop()

n = int(input())
stack = [0]
i = 1
result = []
for _ in range(n):
    num = int(input())
    if stack[-1] == num:
        result.append('-')
        stack.pop()
    elif stack[-1] < num:
        if i > num:
            result = ['NO']
            break
        while stack[-1] < num:
            stack.append(i)
            result.append('+')
            i += 1
        result.append('-')
        stack.pop()
    else:
        result = ['NO']
        break

for c in result:
    print(c)