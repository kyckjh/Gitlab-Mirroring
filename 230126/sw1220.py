import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    arr = []
    result = 0
    N = int(input())
    for i in range(100):
        arr.append(list(map(str, input().split())))
    for i in range(100):
        temp = ''
        for j in range(100):
            if arr[j][i] != '0':
                temp += arr[j][i]
        result += temp.count('12')
    
    
    # result = 0
    # for i in range(100):
    #     temp = 0
    #     tempIndex = 0       
    #     while tempIndex < 100:   
    #         firstN = -1
    #         lastS = -1 
    #         for j in range(tempIndex, 100):
    #             if arr[j][i] == 1:
    #                 firstN = j
    #             if firstN != -1 and arr[j][i] == 2:
    #                 tempIndex = j
    #                 break
    #         for j in range(tempIndex, 100):
    #             if arr[j][i] == 2:
    #                 lastS = j
    #             if lastS != -1 and arr[j][i] == 1:
    #                 tempIndex = j
    #                 break
    #         else:
    #             tempIndex = 100
                
    #         if firstN == -1 or lastS == -1:
    #             break
    #         else:
    #             temp += 1
    #     result += temp        
    print(f'#{test_case}', result)
