students = [
    '박해피',
    '이영희',
    '조민지',
    '조민지',
    '김철수',
    '이영희',
    '이영희',
    '김해킹',
    '박해피',
    '김철수',
    '한케이',
    '강디티',
    '조민지',
    '박해피',
    '김철수',
    '이영희',
    '박해피',
    '김해킹',
    '박해피',
    '한케이',
    '강디티',
]

stu_dict = {}
for student in students:
    if stu_dict.get(student) == None:
        stu_dict[student] = 1
    else:
        stu_dict[student] += 1

result_dict = {}
# 정렬
while(len(stu_dict) > 0):
    max_num = 0
    max_stu = ''
    for name in stu_dict:
        if max_num < stu_dict[name]:
            max_num = stu_dict[name]
            max_stu = name
    result_dict[max_stu] = max_num
    stu_dict.pop(max_stu)
    
print(result_dict)
