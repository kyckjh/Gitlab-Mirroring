class Person():
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1

p1 = Person('길동')
p2 = Person('사임당')
p3 = Person('순신')

print(p1.name)              # 길동
print(p1.population)        # 3 (이렇게 사용할 수도 있지만)
print(Person.population)    # 3 (가급적이면 이렇게 쓰자)

p1.population = 100         # 인스턴스를 통해 접근하면 새로운 인스턴스 변수가 새로 생성됨

print(Person.population)    # 3
print(p1.population)        # 100

Person.population = 200

print(Person.population)    # 200
print(p1.population)        # 100
print(p2.population)