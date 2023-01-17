str_lst = input('문자열을 입력하세요. : ')

str_list = str_lst.lower().split()

print(str_list)
for i in range(len(str_list) - 1):
    if str_list[i][-1] != str_list[i + 1][0]:
        print('Fail')
        break
else:
    print('Pass')