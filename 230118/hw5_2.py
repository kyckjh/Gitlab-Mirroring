import calendar

while(True):
    year = int(input())
    if calendar.isleap(year):
        print('윤년입니다. 연도를 다시 입력해주세요')
    else:
        break
month = int(input())
day = int(input())
dow = calendar.weekday(year, month, day)
dow_lst = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
if dow == 0:
    print('경고 월요일입니다.')
print(f"'년': {year}, '월': {month}, '일': {day}, '요일': '{dow_lst[dow]}'")