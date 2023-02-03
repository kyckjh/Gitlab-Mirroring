class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def get_age(cls, name, year):
        # 입력받은 이름과 23년 기준 나이를 가진 Person 인스턴스 반환
        return Person(name, 2023 - year)    
    
    def check_age(self):
        if self.age < 19:
            return True # 미성년자이면 True 반환
        else:
            return False
    
#Driver's code
person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())
