s_triangle = input()    # 문자열 입력
lst = list(map(int, s_triangle.split(' ')))     # 띄어쓰기 기준으로 리스트 변환
lst.sort()              # 오름차순 정렬
a, b, c = lst           # 가장 긴 변을 c에 저장

if a + b <= c:
    print('삼각형 아님')
elif a == b == c:
    print('정삼각형')
elif a == b or b == c or a == c:
    print('이등변삼각형')
elif a*a + b*b == c*c:
    print('직각삼각형')
else:
    print('삼각형')