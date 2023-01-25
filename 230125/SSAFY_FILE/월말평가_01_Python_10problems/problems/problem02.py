# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    min = 100   # 최소점을 저장할 변수 (100점이 만점이기 때문에 100으로 초기화)
    max = 0     # 최고점을 저장할 변수
    for score in scores:    # 점수 하나씩 비교
        if min > score:     # 현재 비교하는 점수가 저장된 최소점보다 작으면 최소점 업데이트
            min = score
        elif max < score:   # 현재 비교하는 점수가 저장된 최고점보다 크면 최고점 업데이트
            max = score
    return (min, max)       # 최소점과 최고점을 튜플로 리턴
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
