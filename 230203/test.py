import time
start = time.time()  # 시작 시간 저장
 
arr = []
for i in range(10000): 
    print(f'{i}')

 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간