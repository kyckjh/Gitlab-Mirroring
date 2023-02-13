T = int(input())
for t in range(1, T+1):
    chars = input()
    arr = []
    for char in chars:
        if char in ['{', '(']:
            arr.append(char)
        elif char == '}':
            if len(arr) > 0:
                temp = arr.pop()
                if temp != '{':
                    break
            else:
                break
        elif char == ')':
            if len(arr) > 0:
                temp = arr.pop()
                if temp != '(':
                    break
            else:
                break
    else:
        if len(arr) > 0:
            print(f'#{t} 0')
        else:
            print(f'#{t} 1')
        continue
    print(f'#{t} 0')