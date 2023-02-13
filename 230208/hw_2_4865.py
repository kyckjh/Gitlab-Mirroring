T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    result_dict = {}
    for char1 in str1:
        if result_dict.get(char1) == None:
            result_dict.setdefault(char1, 0)
            for char2 in str2:
                if char1 == char2:
                    result_dict[char1] += 1
        else:
            # 이미 찾았으면
            continue
    max_result = 0
    for n in result_dict.values():
        if n > max_result:
            max_result = n
    print(f'#{t} {max_result}')