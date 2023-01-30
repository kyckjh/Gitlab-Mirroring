import random

class ClassHelper:
    def __init__(self, students):
        self.students = students
    def pick(self, n):
        return random.sample(self.students, n)
    def match_pair(self):
        random.shuffle(self.students)
        match_lst = []
        while(len(self.students) > 0):     
            temp_lst = []       
            if len(self.students) % 2:  # 홀수일 때
                for _ in range(3):
                    temp_lst.append(self.students.pop())
            else:
                for _ in range(2):
                    temp_lst.append(self.students.pop())
            match_lst.append(temp_lst)
        return 

ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
