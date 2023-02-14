import sys
sys.stdin = open("input (1).txt", "r")

for tc in range(10):
    t, N = map(int, input().split())
    add1 = [0] * 100 # 주소1 (인덱스 : 출발점, 값 : 도착점)
    add2 = [0] * 100 # 주소2
    result = 0
    nums = list(map(int, input().split()))
    for i in range(0, N*2, 2):  # 입력값 저장
        a, b = nums[i], nums[i+1] # a : 출발점, b : 도착점
        if add1[a] == 0: # 아직 주소가 등록되지 않았으면
            add1[a] = b  # 첫 번째 주소에 저장
        else:
            add2[a] = b  # 두 번째 주소에 저장

    stack = [0]
    visited = [0] * 100
    while stack:
        current = stack[-1]  # 현재 위치(스택의 top)
        visited[current] = 1 # 현재 위치 방문 표시
        if current == 99: # 현재 위치가 도착점이면
            result = 1    # 도착 성공, 반복문 탈출
            break
        des = add1[current] # 현재 위치에서 갈 수 있는 첫 번째 주소
        if des != 0 and visited[des] == 0: # 도착점이 존재하고 방문한 적이 없으면
            stack.append(add1[current])    # 스택에 추가
            continue
        des = add2[current] # 현재 위치에서 갈 수 있는 두 번째 주소
        if des != 0 and visited[des] == 0:
            stack.append(add2[current])
            continue
        stack.pop() # 갈 수 있는 곳이 없으면 스택 pop
    print(f'#{tc+1} {result}')

