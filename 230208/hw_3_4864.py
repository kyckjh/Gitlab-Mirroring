T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 1
    for i in range(len(str2) - len(str1)+1):
        for j in range(len(str1)):
            if str2[i + j] != str1[j]:
                break
        else:
            break
    else:
        result = 0
    print(f'#{t} {result}')
