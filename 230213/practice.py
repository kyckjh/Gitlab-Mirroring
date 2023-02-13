arr_stack = []
s = input()
for ss in s:
    if ss == '(':
        arr_stack.append(ss)
    else:
        if len(arr_stack) == 0:
            print('Error : 스택이 비었습니다.')
        else:
            print(arr_stack.pop())
if len(ss) > 0:
    print(' Error : 스택에 item이 남았습니다.', s)
