# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    y, x = position     # 현재 위치를 x, y 변수에 저장
    # 숫자 M에 따라 각각 좌표 변경
    if M == 0:
        y -= 1
    elif M == 1:
        y += 1
    elif M == 2:
        x -= 1
    elif M == 3:
        x += 1
    # x, y 중 하나라도 범위를 벗어나면 False 리턴, 아니면 True 리턴
    return 0 <= x < N and 0 <= y < N
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
