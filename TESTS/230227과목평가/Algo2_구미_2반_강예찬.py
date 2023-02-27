def check(a, b, k):     # a, b를 기준으로 k만큼 떨어진 위치(가장자리)에 별이 있는지 확인하는 함수
    # amk : a-k좌표, apk : a+k 좌표, bmk : b-k좌표, bpk : b+k좌표 
    # 각각 인덱스 범위를 벗어나지 않도록 초기화
    amk = 0 if a-k < 0 else a-k      
    apk = N-1 if a+k > N-1 else a+k
    bmk = 0 if b-k < 0 else b-k
    bpk = N-1 if b+k > N-1 else b+k
    cnt = 0 # 별의 개수를 저장할 함수
    cnt += arr[amk][bmk:bpk+1].count('*')       # 좌표 기준 위쪽으로 k만큼 떨어진 영역
    cnt += arr[apk][bmk:bpk+1].count('*')       # 좌표 기준 아래쪽으로 k만큼 떨어진 영역
    cnt += arr_t[bmk][amk:apk+1].count('*')     # 좌표 기준 왼쪽으로 k만큼 떨어진 영역
    cnt += arr_t[bpk][amk:apk+1].count('*')     # 좌표 기준 오른쪽으로 k만큼 떨어진 영역
    return cnt # 범위 내에서 찾은 별 개수 반환

T = int(input())
for t in range(1, T+1):
    # N : 하늘의 전체 크기, K : 영역의 크기(K*K), (A, B) : 초점
    N, K, A, B = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(N)] # 하늘(별)의 정보 입력받기
    arr_t = list(zip(*arr))  # 열끼리 계산하기 위한 전치행렬

    # 영역의 가장자리는 위, 아래, 오른쪽, 왼쪽으로 초점 기준으로 K//2씩 떨어져 있음
    K //= 2     # 좌표 기준으로 K*K 영역의 가장자리를 탐색하기 위해 2로 나눔

    for k in range(K+1, N): # 촬영할 수 없는 범위(K*K의 영역을 벗어난 곳) 먼저 검사
        result = check(A, B, k)
        if result:  # 별 개수가 0이 아니면 촬영 가능 영역 밖에 별이 있어
            print(f'#{t} -1') # 모든 별을 촬영할 수 없다는 뜻이므로 -1 출력
            break
    else: # 범위 밖에 별이 없으면
        for k in range(K, -1, -1):
            result = check(A, B, k)     # 초점 기준 k만큼 떨어진 가장자리에 별이 있는지 검사
            if result:                  # 탐색한 가장자리에 안에 별이 있으면
                # k는 K부터 시작해서 확대할 때 마다 1씩 작아지므로 확대한 횟수는 K-k
                print(f'#{t} {K-k}')    # 확대한 횟수 출력
                break
        else: # 별이 아예 없을 때
            print(f'#{t} -1')