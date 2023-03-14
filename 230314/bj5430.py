import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input()         # 수행할 함수 p (예 : RDDRD)
    n = int(input())    # 배열에 들어있는 수 n
    arr = input()       # 정수로 이루어진 배열 (문자열로 입력 받음)
    if n > 0:           # n이 0보다 크면 문자열을 정수 배열로 변환
        arr = list(map(int, arr[1:-2].split(',')))
    else:               # n이 0이면
        if 'D' in p:    # 수행할 함수에 D가 들어있으면 n이 0이라서 뺄 정수가 없으므로
            print('error')  # error 출력
        else:           # 수행할 함수에 D가 없으면
            print('[]') # 빈 리스트 출력
        continue        # 다음 testcase로 넘어감
    first = -1  # 맨 앞 인덱스
    last = n    # 맨 뒤 인덱스
    isReverse = False   # 배열이 뒤집혔는지 확인하는 변수
    for order in p:
        if order == 'R':    # 수행할 함수가 R이면
            isReverse = not isReverse   # 배열 뒤집기
        elif order == 'D':      # D일때            
            if isReverse:       # 배열이 뒤집혀있으면
                last -= 1       # 맨 뒤 인덱스 하나 감소
            else:               # 배열이 안뒤집혔으면
                first += 1      # 맨 앞 인덱스 하나 증가
            if first == last:   # 맨 앞과 맨 뒤 인덱스가 같아졌다면 더 이상 뺄 정수가 남아있지 않은 상태에서 뺐다는 뜻이므로
                print('error')  # error 출력 후 break
                break
    else:   # break 없이 끝까지 실행되었다면
        result = arr[first+1:last]  # 배열에서 빠진 수 제외하기
        if isReverse:               # 배열이 뒤집혀있다면
            result.reverse()        # 배열 뒤집기
        ans = "["+",".join(map(str, result))+"]"    # 출력할 문자열 만들기
        print(ans)

'''
5
RDD
4
[11,22,33,44]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
RD
3
[12, 34, 56]
'''

