import sys
input = sys.stdin.readline

# 해당 좌표의 빈 칸에 들어갈 수 있는 값들을 배열로 반환하는 함수
def check(y, x):    
    lst = [1]*10        # 빈 칸에 들어갈 수 있는 숫자 후보들
    for i in range(9):  # 해당 좌표의 열과 행 검사
        lst[arr[y][i]] = 0  # 같은 열에 있는 숫자 후보에서 제외
        lst[arr[i][x]] = 0  # 같은 행에 있는 숫자 후보에서 제외
    # 3x3 정사각형 검사
    x = (x//3)*3
    y = (y//3)*3
    for i in range(y, y+3):
        for j in range(x, x+3):
            lst[arr[i][j]] = 0  # 같은 정사각형 안에 있는 숫자 후보에서 제외
    result = []     # 반환할 값을 저장할 배열
    for i in range(1, 10):  # 후보들 인덱스 1~9까지
        if lst[i]:          # 값이 1이면 (후보에서 제외되지 않았으면)
            result.append(i)    # 반환할 배열에 추가
    return result   # 해당 좌표에 들어갈 수 있는 값들 배열로 반환

def dfs(i, k):  # i : 지금까지 채운 빈 칸의 수, k : 총 채워야 할 빈 칸의 수 - 1
    if i == k:  # 마지막 칸을 채워야 할 때
        y, x = zeros[i] # 마지막 칸의 좌표
        last = check(y, x)  # 마지막 칸에 넣을 수 있는 값들
        if not last:        # 넣을 수 있는 값이 없을 때
            return          # 이전 칸으로 돌아가기
        arr[y][x] = last[0] # 넣을 수 있는 값이 있다면 제일 작은 값 넣기 (아무 값이나 넣어도 됨)
        for i in range(9):  # 스도쿠 판 출력하기
            print(*arr[i])
        return
        
    y, x = zeros[i]     # 이번에 채울 빈 칸의 좌표
    lst = check(y, x)   # 이 칸에 들어갈 수 있는 값들의 배열
    while lst:          # 빈칸에 넣을 수 있는 값이 남아있을 때
        num = lst.pop() # 배열에서 하나 꺼내기
        arr[y][x] = num # 빈칸에 넣기
        dfs(i+1, k)     # 다음 칸 채우러 가기
    
    # 더 이상 넣을 수 있는 값이 없거나 모두 넣어봤을 때
    arr[y][x] = 0   # 이전 칸으로 돌아가기 전에 빈칸 지우기
    return          # 이전 칸으로 돌아가기

# 스도쿠 판
arr = [list(map(int, input().split())) for _ in range(9)]
zeros = [] # 스도쿠의 빈 칸 좌표들을 저장할 배열
for i in range(9):
    for j in range(9):
        if not arr[i][j]:   # 칸의 값이 0이면
            zeros.append((i, j))    # 배열에 좌표 추가

# 빈 칸을 모두 채울 때 까지 dfs 실행
dfs(0, len(zeros)-1)    