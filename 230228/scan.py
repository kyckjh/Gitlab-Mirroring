import sys
sys.stdin = open("sample_input.txt", "r")

code_num = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}

def htob(inputs): # 16진수에서 이진수로 변환해주는 함수
    result = ''
    for n in inputs:
        for i in range(4):
            result += '1' if 8 >> i & int(n, 16) else '0'
    return result.strip('0') # 문자열로 반환, 앞뒤에 0 제거

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    answer = 0 # 답
    i = 0
    while i < len(arr)-1: # 입력된 값에서 중복되는 행 제거
        if arr[i] == arr[i+1]:
            del arr[i]
            continue
        i += 1
    codes = set() # 입력값에서 뒤에 0 모두 제거해서 codes에 넣음
    for code in arr:    # 입력값 한 행씩 검사
        i = M-1         # 마지막 인덱스부터 검색
        while i >= 0:   # 인덱스가 0보다 클 때 검색
            if code[i] != '0':  # 1을 찾으면
                codes.add(code[0:i+1])  # 1이 있는 곳 까지만 슬라이스 해서 codes에 넣음
                # 예시
                # code        : 000000328D1AF6E4C9BB0000000196EBC5A316C57800000000
                # code[0:i+1] : 000000328D1AF6E4C9BB0000000196EBC5A316C578
                break
            i -= 1      # 못찾으면 다음 인덱스로
    code_set = set()
    for code in codes:
        result = htob(code) # result : 11010001011010001101101110110111001001101000110111101
        while len(result)%56 != 0:
            result = '0' + result
        # 56의 배수로 맞춰서 앞에 0 넣어주기 -> result : 00011010001011010001101101110110111001001101000110111101
        cnt = 0             # cnt : 값이 0에서 1 또는 1에서 0으로 바뀔 때 마다 증가
        prev = result[len(result)-1]    # prev : 이전 값 (값이 바뀌는 것 탐지용)
        i = len(result)-1   # 시작 인덱스(마지막부터)
        temp_lst = []       # 1과 0의 비율을 넣을 리스트 (예시 : [1, 1, 4, 1, 2, 3, 1, 1, 2, 2, 1, 2, 3, 1, 2, 1, 3, 1, 2, 1, 2, 3, 1, 1, 2, 1, 1, 3, 1, 1, 2, 3])
        last = len(result)  # 탐색 시작한 곳 저장
        while i > -1:
            if len(temp_lst) == 31:   # 암호가 8자리 이므로 비율은 항상 32개가 되야 함. 31개가 되었을 때 나머지는 모두 0이므로 탐색 중지
                min_v = min(temp_lst) # 비율의 최소값
                plus = 56*min_v-(last-i-1)  # 56*min_v : 암호를 이진수로 바꿨을 때 총 길이, last-i-1 : 지금까지 찾은 이진수의 길이
                temp_lst.append(plus)       # plus : 남은 0의 개수
                temp_lst = temp_lst[::-1]   # 마지막부터 비율을 넣었으므로 거꾸로 바꿔주기
                for k in range(0, len(temp_lst)):
                    temp_lst[k] //= min_v   # 비율을 최소값으로 나눠주기
                    #  나누기 전 [2, 2, 6, 4, 4, 2, 4, 4, 2, 4, 2, 6, 2, 4, 6, 2, 2, 4, 2, 6, 4, 2, 4, 4, 2, 6, 2, 4, 6, 4, 2, 2], 최소값이 2
                    #  나누기 후 [1, 1, 3, 2, 1, 3, 1, 2, 1, 1, 3, 2, 1, 4, 1, 1, 1, 1, 3, 2, 2, 1, 2, 2, 1, 2, 3, 1, 3, 2, 1, 1]
                code_result = []            # 비율에서 암호코드로 바꾼 후 넣을 리스트 (예시 : [0, 9, 4, 8, 8, 2, 4, 3])
                for k in range(0, len(temp_lst)-3, 4):
                    code_result.append(code_num[(temp_lst[k],temp_lst[k+1],temp_lst[k+2],temp_lst[k+3])])
                code_set.add(tuple(code_result)) # 암호코드를 code_set에 저장하기 위해 tuple로 바꿈, set이므로 중복을 없앰
                temp_lst = [] # 비율 리스트 초기화
                while i > 0 and result[i] == '0': # 다음 1을 찾을 때 까지 인덱스 감소
                    i -= 1
                prev = '1'
                cnt = -1 # 카운트 초기화, while문 시작할 때 cnt가 증가하므로 -1로 시작
                i += 1   # while문이 시작할 때 i가 감소하므로 1 더하기
                last = i # 다음 암호 코드의 마지막 인덱스 저장
                continue
            i -= 1      # 다음 인덱스 검색
            cnt += 1    # 카운트 증가
            if result[i] != prev: # 이전 문자열과 다르면 (0에서 1로, 1에서 0으로 바뀔 때)
                temp_lst.append(cnt) # 비율 리스트에 cnt 저장
                prev = result[i]     # 이전 문자열 저장
                cnt = 0              # 카운트 초기화
    for lst in code_set: # 코드마다 유효성 검사 및 출력할 답에 추가, 예시 - lst : (0, 9, 4, 8, 8, 2, 4, 3)
        num1 = 0    # 홀수번째 값의 합
        num2 = 0    # 짝수번째 값의 합
        for i in range(len(lst)):
            if i % 2:
                num1 += lst[i]
            else:
                num2 += lst[i]
        if (num1+num2*3)%10 == 0:   # 홀수합 + 짝수합*3이 10의 배수이면 출력할 답에 추가
            answer += num1+num2
    print(f'#{t} {answer}')

