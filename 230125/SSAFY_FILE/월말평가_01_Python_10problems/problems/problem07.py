# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    pi = 3.14   
    if len(numbers) == 1:   # 입력 값이 1개일 때
        return numbers[0] * numbers[0] * pi     # 반지름 * 반지름 * 원주율
    elif len(numbers) == 2: # 입력 값이 2개일 때
        if sum(numbers) % 2 != 0:       # 입력 값의 합이 홀수이면
            return numbers[0] * numbers[1] * 0.5    # 밑변길이 * 높이 / 2
        return numbers[0] * numbers[1]  # 짝수이면 밑변길이 * 높이
    elif len(numbers) > 2:      # 입력값이 3개 이상일 때
        sum_num = sum(numbers)  # 모든 입력의 합
        average_num = sum_num / len(numbers)    # 모든 입력의 평균
        return (sum_num, average_num)   # 합과 평균을 튜플로 리턴
    else:
        return 0
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0