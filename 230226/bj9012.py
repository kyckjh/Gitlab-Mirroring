import sys
T = int(sys.stdin.readline())
for _ in range(T):
    arr = list(map(str,sys.stdin.readline().strip()))
    stack = []
    for char in arr:
        if char == '(':
            stack.append(1)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')