# key : 찾을 쪽 번호, pages : 전체 쪽 수
def binary_search(key, pages):
    cnt = 0 # 탐색 횟수
    l = 1   # 검색 구간의 왼쪽
    r = pages   # 검색 구간의 오른쪽
    mid = int((l+r)/2) # 중간 페이지 (1 + 11 = 6, 1 + 12 = 6)
    while mid != key:  # key를 찾을 때 까지 반복
        cnt += 1 # 탐색 횟수 증가
        if key > mid: 
            l = mid
        else:
            r = mid
        mid = int((l+r)/2)
    return cnt  # 탐색 횟수 반환

T = int(input())    # 테스트 케이스 수
for t in range(1, T+1):
    # P : 전체 쪽 수, A : A가 찾을 쪽 번호, B : B가 찾을 쪽 번호
    # 1 <= P, A, B <= 1000
    P, A, B = map(int, input().split())
    a = binary_search(A, P) # A가 탐색한 횟수 반환
    b = binary_search(B, P) # B가 탐색한 횟수 반환
    print(f'#{t}', end=' ')
    if a == b:  # 비겼을 때
        print(0)
    elif a < b: # A가 먼저 찾았을 때
        print('A')
    else:       # B가 먼저 찾았을 때
        print('B')
