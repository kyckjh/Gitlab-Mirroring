
import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    dump_cnt = int(input()) # 덤프 가능한 횟수
    boxes = list(map(int, input().split()))   # 상자 높이값 리스트
    diff = 100 # 최고점과 최저점의 차이    
    while dump_cnt > 0 and diff > 1:      
        maxV = 0
        minV = 100
        max_lst = []   # 최고점 박스 리스트 , 인덱스 저장
        min_lst = [] # 최저점 박스 리스트
        for i in range(100):
            if boxes[i] > maxV:   # 최고점 보다 현재 박스가 높으면
                maxV = boxes[i]
                max_lst = [i]    # 최고점 리스트 변경
            elif boxes[i] == maxV:    # 같으면 추가
                max_lst.append(i)
            if boxes[i] < minV:   # 최저점 보다 현재 박스가 낮으면
                minV = boxes[i]
                min_lst = [i]    # 최고점 리스트 변경
            elif boxes[i] == minV:    # 같으면 추가
                min_lst.append(i)
        while len(max_lst) > 0 and len(min_lst) > 0:    # 최저점 리스트와 최고점 리스트에 모두 값이 존재하면
            # 최고, 최저점 리스트에서 하나씩 값을 빼서 인덱스만 전달
            boxes[max_lst.pop()] -= 1 # 가장 높은 박스의 위치에서 하나 뺌
            boxes[min_lst.pop()] += 1  # 가장 낮은 박스의 위치에서 하나 더함
            if len(max_lst) == 0:
                maxV -= 1
            if len(min_lst) == 0:
                minV += 1
            diff = maxV - minV
            dump_cnt -= 1
            if dump_cnt == 0 or diff < 2: 
                break
    print(f'#{t} {diff}')