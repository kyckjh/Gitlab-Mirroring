import sys
input = sys.stdin.readline

def calc(v1, v2, op):   # v1 연산자(op) v2 의 결과 반환
    if op == 0: # 더하기 연산
        return v1 + v2
    if op == 1: # 빼기 연산
        return v1 - v2
    if op == 2: # 곱하기 연산
        return v1 * v2
    # 나누기 연산
    if v1 < 0:  # 앞 숫자가 음수인 경우
        v1 *= -1    # 먼저 양수로 바꾼 뒤
        return -(v1 // v2)  # 나눈 결과를 다시 음수로 바꾸어 반환
    return v1//v2   # 앞 숫자가 양수인 경우 그냥 나누기 연산하여 반환

def dfs(i, k, sum_v):
    global max_v
    global min_v
    if i == k:  # 모든 연산이 끝났을 때 최댓값 최솟값 갱신
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)
    for j in range(4):  # 연산자 남은 수 검사
        if arr2[j]:     # 연산자의 수가 남아 있으면
            arr2[j] -= 1    # 연산자 수 하나 감소
            dfs(i+1, k, calc(sum_v, arr1[i], j))    # 연산한 결과를 dfs함수에 전달
            arr2[j] += 1    # 연산자 수 되돌리기

N = int(input())
max_v = -1000000001 # 최댓값을 저장할 변수
min_v = 1000000001  # 최솟값을 저장할 변수
arr1 = list(map(int, input().split()))  # 연산할 숫자 입력받기
arr2 = list(map(int, input().split()))  # 연산자의 수(더하기, 빼기, 곱하기, 나누기) 입력받기
dfs(1, N, arr1[0])  # 첫 번째 숫자부터 시작
print(max_v)
print(min_v)