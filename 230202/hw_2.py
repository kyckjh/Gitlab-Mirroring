T = int(input())
for t in range(1, T + 1):
    # K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # N : 종점 정류장
    # M : 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split()) 
    stations = list(map(int, input().split()))
    stations.append(N)  # 종점 추가
    cnt = 0 # 충전 횟수
    current = 0 # 현재 station
    for i in range(M + 1):
        # 종점 바로 전 역이 아니고, 다다음 역까지 거리가 K보다 작거나 같을 때
        if i < M and stations[i + 1] - current <= K: 
            continue
        if stations[i] - current <= K:   # 다음 역까지의 거리가 K보다 작거나 같을 때
            if i == M: # 다음 역이 종점이면
                break   # 종점에서는 충전 필요 X
            current = stations[i]
            cnt += 1        
        else:   # 다음 역까지의 거리가 K보다 클 때
            cnt = 0
            break
    print(f'#{t} {cnt}')