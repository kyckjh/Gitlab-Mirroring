import math
print('게시글의 총 갯수를 입력하세요 : ', end = '')
total = int(input())
print('한 페이지에 필요한 게시글 수를 입력하세요 : ', end = '')
num = int(input())
print(math.ceil(total / num))