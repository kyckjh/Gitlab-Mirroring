T = int(input())
for t in range(1, T+1):
    # N, M : 행과 열의 수 입력 받기
    N, M = map(int, input().split())
    # 나무의 비용 정보 입력받기
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = list(zip(*arr)) # 열끼리 계산하기 위해 행과 열 바꾸기
    sum_v = 0       # 나무를 심기 위한 총 비용
    sum_tree = 0    # 총 심은 나무의 수
    max_v = 0       # 가장 비싼 나무의 가격
    max_col = 0     # 가장 비싼 나무가 심겨져 있는 열 번호
    for i in range(0, M, 2):    # 각 행을 두 칸 간격으로 실행
        sum_v += sum(arr[i])    # 행과 열을 바꿨으므로 각 행의 합을 총 비용에 추가
        sum_tree += N           # 심은 나무의 수는 한 행마다 행(행과 열 바꾸기 전)의 개수를 추가
        temp_max = max(arr[i])  # 해당 행에서 가장 비싼 나무의 값을 찾기
        if max_v <= temp_max:   # 이전에 찾은 가장 비싼 나무와 비교해서 더 비싸거나 같으면
            max_v = temp_max    # 가장 비싼 나무 가격 갱신
            max_col = i         # 가장 비싼 나무가 있는 열 번호도 갱신, 행과 열을 바꿨으므로 행의 인덱스를 넣어줌

    # 열 번호가 1부터 시작하므로 가장 비싼 나무가 있는 열 번호에 1을 더해줌
    print(f'#{t} {sum_v} {sum_tree} {max_v} {max_col+1}')