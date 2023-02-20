T = int(input())
for t in range(1, T+1):
    N = int(input())
    cnts = [0]*200
    for _ in range(N):
        s, e = map(int, input().split())
        if s>e:
            s,e = e,s
        for i in range((s-1)//2, (e-1)//2+1):
            cnts[i] += 1
    ans = max(cnts)
    print(f'#{t} {ans}')

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
30 50'''