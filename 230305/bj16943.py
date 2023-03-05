import sys
def perm(cnt): 
    global max_v
    if cnt == N:    # N번 고르면 끝
        c = int("".join(C)) # 저장한 순열 int형으로 바꾸기
        if c < int(B):  # C가 B보다 작으면
            max_v = max(c, max_v)   # 최대값과 비교해서 저장
        return
    for i in range(N):  # A에서 N번 골라서 C에 저장하기
        # 이미 골랐거나 맨 앞이 0이면 건너뛰기
        if select[i] or (cnt == 0 and A[i] == '0'):
            continue
        select[i] = 1   # 골랐다는 표시
        C[cnt] = A[i]   # 순열에 고른 값 저장
        perm(cnt+1)     # cnt : 고른 개수
        select[i] = 0   # 골랐다는 표시 제거

A, B = sys.stdin.readline().split() # 순열로 만들기 쉽도록 문자열로 읽기
N = len(A)
select = [0]*N  # 순열을 만들기 위한 배열(선택여부 저장)
C = [0]*N       # 순열을 저장하기 위한 배열
max_v = -1      # B보다 작은 C의 최대값 저장
perm(0) # A의 가능한 모든 순열 계산(맨 앞에 0이 오는 경우 제외)
print(max_v)