isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
icp = {'*':2, '/':2, '+':1, '-':1, '(':3}
# '2+3*4/5'
data = '2+3*4/5'

# 우선순위가 높으면 stack에 넣어주기
stack = []
for i in range(len(data)):
    if data[i] in '0123456789':
        print(data[i], end='')
    else:
        if data[i] == ')':
            while stack[-1] != '(':
                print(stack.pop(), end=' ')
            stack.pop()
        elif not stack:
            stack.append(data[i])
        else:
            if isp[stack[-1]] < icp[data[i]]:
                stack.append(data[i])
            else:
                while stack and isp[stack[-1]] >= icp[data[i]]:
                    print(stack.pop(), end='')
                stack.append(data[i])

while stack:
    print(stack.pop(), end='')
print()
