import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    N = int(input())
    stack = []  # 연산자 스택
    result = [] # 후위표기식으로 변환된 식
    s = input() # 입력된 식
    for char in s:
        if char in '1234567890': # 숫자면 바로 결과에 저장
            result.append(char)
        else: # 연산자면
            if not stack: # 스택이 비었으면 스택에 추가
                stack.append(char)
            else: # 스택이 비어있지 않으면
                if char == '+': # '+'면 스택을 비우고 결과에 저장
                    while stack:
                        result.append(stack.pop())
                else: # '*' 일 때
                    if stack[-1] != '+': # 스택 맨 위에 '+'면 빼고 결과에 저장
                        result.append(stack.pop())
                stack.append(char) # 스택에 연산자 저장

    while stack: # 남은 연산자 모두 결과에 저장
        result.append(stack.pop())

    # 후위표기식 계산
    for char in result:
        if char in '1234567890': # 숫자면 스택에 저장
            stack.append(int(char))
        else: # 연산자면 스택에서 숫자 두 개 빼서 계산 후 스택에 다시 저장
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            else:
                stack.append(stack.pop() * stack.pop())

    print(f'#{t} {stack[0]}')

