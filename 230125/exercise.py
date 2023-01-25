# 주어진 문자열에서 숫자, 문자, 기호가 각각 몇개인지 판단하는 함수

def check(target_str):
    dec_num = 0
    alpha_num = 0
    other = 0
    for char in target_str:
        if char.isdecimal():
            dec_num += 1
            continue
        elif char.isalpha():
            alpha_num += 1
            continue
        else:
            other += 1
    return f'숫자 : {dec_num}개 문자 : {alpha_num}개 기호 : {other}개'
            
target = '숫자3개, 문자9개, 기호4개'
print(check(target))