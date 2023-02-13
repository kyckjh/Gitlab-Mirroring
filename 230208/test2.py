#one = ord('1')
#print(one)
#print(chr(one))

# 문자 받아와서 숫자로 반환하기
def atoi(data):
    num = 0
    for char in data:
        temp = ord(char) - ord('0')
        num = num*10 + temp
    return num


result = atoi('12030')
print(result)


def itoa(data):
    result = ''
    while data > 0:
        temp = data % 10
        char = chr(temp + ord('0'))
        result = char + result
        data //= 10
    return result


result = itoa(10230)
print(result)