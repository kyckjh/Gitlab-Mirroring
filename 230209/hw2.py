T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    lenA = len(A)
    lenB = len(B)
    i = 0
    typing = lenA
    while i <= lenA - lenB:
        skip = lenB # 넘어갈 개수
        for j in range(lenB-1, -1, -1): # 단어 마지막부터 비교
            if A[i+j] != B[j]:  # 다른글자면...
                idx = 0
                for b in range(j):   # 찾는 단어에 글자가 있는지 확인
                    if A[i+j] == B[b]:  # 같은 글자가 있으면
                        skip = j - b
                break
        else:   # 같은 단어를 찾으면 타이핑 수 줄이고 lenB 만큼 넘어가기
            typing -= lenB-1
            skip = lenB
        i += skip
    print(f'#{t} {typing}')

'''
5
banana bana
asakusa sa
asdfasssda as
kkkkssssss aaas
bbbkddsdasd dasd
'''