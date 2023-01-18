year = int(input())
result = False
if year % 4 == 0 and year % 100 != 0:
    result = True
elif year % 400 == 0:
    result = True
print(f'{year}년은 윤년입니다.' if result else f'{year}년은 윤년이 아닙니다.')