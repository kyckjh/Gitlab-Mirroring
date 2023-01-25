# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over_24(people):
    num_over_24 = 0     # 24세를 초과하는 지원자 수를 저장할 변수
    for man in people:  # 리스트의 한 사람(딕셔너리)씩 for문으로 돌기
        age = man['age']    # 딕셔너리에서 'age'를 key로 가진 value를 age에 저장
        if age > 24:        # age가 24를 넘으면 변수에 1씩 추가
            num_over_24 += 1
    return num_over_24
    
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    people = [
        {'name': '김싸피', 'age': 25},
        {'name': '이싸피', 'age': 28},
        {'name': '조싸피', 'age': 29},
        {'name': '아싸피', 'age': 23},
        {'name': '최싸피', 'age': 22},
        {'name': '고싸피', 'age': 21},
        {'name': '유싸피', 'age': 26},
        {'name': '후싸피', 'age': 20},
    ]

    print(over_24(people))  # 4