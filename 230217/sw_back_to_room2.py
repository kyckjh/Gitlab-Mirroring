T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0]*201
    for i in range(N):
        a, b = map(lambda x: (int(x)+1)//2, input().split())
        if a > b:
            a,b = b,a
        for i in range(a, b):
            arr[i] += 1
    print(f'#{t} {max(arr)}')

'''
3  
4  
10 20 
30 40
50 60
70 80
2 
1 3
2 200
3
10 100
20 80
30 50
'''