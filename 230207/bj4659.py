vowels= ['a', 'e', 'i', 'o', 'u']
while True:
    password = input()
    if password == 'end':
        break
    v_cnt = 0
    for vs in vowels:
        v_cnt += password.count(vs)
    if v_cnt == 0:
        print(f'<{password}> is not acceptable.')
        continue
    v_cnt = 0   # 모음 카운트
    c_cnt = 0   # 자음 카운트
    lastChar = ''
    result = True
    for char in password:
        if char in vowels:
            v_cnt += 1
            c_cnt = 0
        else:
            c_cnt += 1
            v_cnt = 0
        if v_cnt == 3 or c_cnt == 3:
            result = False
            break
        
        if lastChar == char:
            if char == 'e' or char == 'o':
                continue
            else:
                result = False
                break
        lastChar = char
    if result:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')