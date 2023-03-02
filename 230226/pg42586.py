def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0
    while cnt < len(progresses):
        if progresses[cnt]+speeds[cnt]*day<100:
            day += 1
            continue
        cnt += 1
        while cnt < len(progresses) and progresses[cnt]+speeds[cnt]*day >= 100:
            cnt += 1
        answer.append(cnt)
    for i in range(len(answer)-1, 0, -1):
        answer[i] -= answer[i-1]
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))