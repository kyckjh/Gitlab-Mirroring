# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    chars = ''  # 암호화된 글자를 저장할 변수
    for char in word:   # 단어의 한 글자씩 for문 반복
        ascii_num = ord(char)   # 글자의 아스키코드 저장
        ascii_num += n          # 아스키코드에 n만큼 더하기
        if char.islower():      # 소문자이면
            if ascii_num > 122: # 밀려난 글자가 알파벳 범위를 넘어가면
                ascii_num -= 26 # 처음으로 돌아오기(알파벳 개수만큼 빼기)
        else:                   # 대문자이면
            if ascii_num > 90:  # 밀려난 글자가 알파벳 범위를 넘어가면
                ascii_num -= 26 # 처음으로 돌아오기
        chars = f'{chars}{chr(ascii_num)}'  # 변수의 뒤에 한 글자씩 추가하기  
    return chars
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
