T = int(input())    # testcase 의 수
for t in range(1, T + 1):
    N = int(input())    # 카드 장 수
    nums = input()      # 카드 숫자 문자열
    count = [0] * 10    # 카드 숫자별 카운트
    for num in map(int, nums):  # 카드 숫자 한 글자씩 int로 읽기
        count[num] += 1 # 카드 숫자를 인덱스로 하는 카운트 리스트에 추가
    maxCard = 0 # 가장 많은 카드에 적힌 숫자
    maxNum = 0  # 가장 많은 카드의 장 수
    for i in range(len(count)):
        if maxNum <= count[i]:
            maxCard = i
            maxNum = count[i]            
    print(f'#{t} {maxCard} {maxNum}')