import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    arr = []
    N = int(input())
    for i in range(100):
        arr.append(list(map(int, input().split())))
    result = 0
    for i in range(100):
        temp = 0
        firstN = -1
        firstS = -1
        for j in range(100):    # 세로로 내려가면서 확인
            if arr[j][i] == 1:  # 제일 처음 나오는 N의 세로 인덱스 저장
                firstN = j
                break
        for j in range(99, -1, -1): # 제일 처음 나오는 S의 세로 인덱스 저장
            if arr[j][i] == 2:
                firstS = j
                break
        if firstN == -1 or firstS == -1:    # N 또는 S 둘 중 하나라도 없으면 다음 가로줄로 넘어감
            continue
        elif firstN > firstS:   # 처음 오는 N이 처음 오는 S보다 밑에 있으면 넘어감
            continue
        for j in range(firstN, firstS + 1): # 처음 N과 처음 S사이에 있는 모든 자성체 세기
            if arr[j][i] != 0:
                temp += 1
        result += temp
        
    print(f'#{test_case}', result)
    

# N극
# 1 : N극
# 2 : S극
# 1 : N극
# S극