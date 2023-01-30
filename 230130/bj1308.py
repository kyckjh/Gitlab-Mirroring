from datetime import datetime

year1, month1, date1 = map(int, input().split())
today = datetime.strptime(f'{year1:0>4}{month1:0>2}{date1:0>2}', '%Y%m%d')
year2, month2, date2 = map(int, input().split())
campday = datetime.strptime(f'{year2:0>4}{month2:0>2}{date2:0>2}', '%Y%m%d')

date_diff = campday - today

if year1 + 1000 < year2:
    print('gg')
elif year1 + 1000 == year2:
    if month1 < month2:
        print('gg')
    elif month1 == month2:
        if date1 <= date2:
            print('gg')
        else:
            print(f'D-{date_diff.days}')
    else:
        print(f'D-{date_diff.days}')
else:
    print(f'D-{date_diff.days}')
