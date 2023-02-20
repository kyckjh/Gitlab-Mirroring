T = int(input())        # 테스트 케이스 수 입력받음
for t in range(1, T+1): # 테스트 케이스 수 만큼 코드 실행
    N = int(input())    # 영역의 크기 입력 받음

    # 조건1 - 로봇은 NxN 구역을 벗어날 수 없다.
    # 영역 가장자리를 -1로 둘러싸며 입력받음
    arr = [[-1] * (N+2)]
    for _ in range(N):
        arr.append([-1] + list(map(int, input().split())) + [-1])
    arr.append([-1] * (N+2))
    # 영역을 -1로 둘러쌌으므로 현재 위치 1, 1부터 시작
    cy = 1
    cx = 1
    # 0 : 오른쪽, 1 : 아래쪽, 2 : 왼쪽, 3 : 위쪽
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ans = [] # 결과를 저장할 배열
    while arr[cy][cx] > -1:     # 현재 위치의 값이 -1이 아닐 때 반복
        ans.append(arr[cy][cx]) # 현재 위치의 값을 결과에 추가
        dir_idx = arr[cy][cx]   # 현재 위치에서 갈 수 있는 방향
        # 조건3 - 로봇은 지나간 구역은 다시 지나지 않는다.
        arr[cy][cx] = -1        # 현재 위치의 값을 -1로 바꿔서 다시 올 수 없게 만들기
        # 다음 위치로 이동
        cy += dir[dir_idx][0]
        cx += dir[dir_idx][1]

    # 이전 인덱스와 같은지 비교하기 위해 첫 번째 값은 그냥 출력
    print(f'#{t} {ans[0]}', end=' ')
    for i in range(1, len(ans)): # 2번째 값부터 마지막까지 출력
        # 조건 - 로봇은 처음 이동할 때와 새로운 방향으로 바꿀 때만 많은 에너지가 든다.
        if ans[i] != ans[i-1]:   # 이전 값이랑 같지 않을 때만 출력(중복된 방향 제거)
            print(ans[i], end=' ')
    print()