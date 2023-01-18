# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

input_list = [1, 1, 3, 3, 0, 1, 1]

last_num = -1
result = []
for num in input_list:
    if num == last_num:
        continue
    else:
        result.append(num)
        last_num = num
print(result)
    