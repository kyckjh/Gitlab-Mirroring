# n : 이전에 뽑은 문자, cnt : 뽑은 개수
def f(n, cnt):   
    global result
    if cnt == N:    # N개 뽑았을 때 r_set에 저장
        r_set.add(result)
        return
    for i in range(n, 4):   # 중복을 피해서 만들기 위해 n부터 뽑기
        result += arr[i]    # 뽑은 문자가 나타내는 수를 더하기
        f(i, cnt+1)         # 다음 문자 뽑기
        result -= arr[i]    # 다음 수 뽑기 전에 더해준 수 빼기

import sys
result = 0  # 만들 수 있는 숫자
r_set = set()   # 만들 수 있는 숫자의 종류를 저장할 set(중복을 피하기 위해 set 사용)
arr = [1, 5, 10, 50]    # 문자의 종류
N = int(sys.stdin.readline())
f(0, 0)
print(len(r_set))