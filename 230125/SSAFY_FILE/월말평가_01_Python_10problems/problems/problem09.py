# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    if number < 2:  # 몫이 2 미만이 되면 리턴 (무조건 1)
        return f'{number}'
    return f'{dec_to_bin(number // 2)}{number % 2}' # 재귀함수의 리턴값 뒤에 2로 나눈 나머지를 붙여 리턴
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
