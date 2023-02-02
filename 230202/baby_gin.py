arr = [2, 1, 3, 3, 4, 5]

for i in range(6): # 0, 1, 2    i : 첫 번째 자리
    for j in range(6):  # j : 두 번째 자리
        if j != i:
            for k in range(6):  # k : 세 번째 자리
                if k != i and k != j:
                    for a in range(6):  # k : 세 번째 자리
                        if a != i and a != j and a!= k:
                            for b in range(6):  # k : 세 번째 자리
                                if b != i and b != j and b!= k and b != a:
                                    for c in range(6):  # k : 세 번째 자리
                                        if c != i and c != j and c!= k and c != a and c != b:                                          
                                            run_cnt = 0
                                            tri_cnt = 0
                                            if arr[a] == arr[b] - 1 and arr[a] == arr[c]-2:
                                                run_cnt += 1
                                            elif arr[a] == arr[b] and arr[a] == arr[c]:
                                                tri_cnt += 1
                                            if arr[i] == arr[j] - 1 and arr[i] == arr[k]-2:
                                                run_cnt += 1
                                            elif arr[i] == arr[j] and arr[i] == arr[j]:
                                                tri_cnt += 1    
                                            else:
                                                pass
                                            if tri_cnt + run_cnt == 2:
                                                print('baby-gin!')
                                                print(arr[i], arr[j], arr[k], arr[a], arr[b], arr[c])