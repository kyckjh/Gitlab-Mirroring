class Person():    
    population = 0
    
    def say_hello(self):    # 인스턴스 메서드
        print(self.name)    
    
    # 매직메서드    
    # 생성자 (Constructor) : 인스턴스 변수 초기화
    def __init__(self, name):   # 얘도 인스턴스 메서드 (self를 받음)
        self.name = name
        Person.population += 1
    def __str__(self):  # 클래스를
        return f'내 이름은 {self.name}'
    
    # 클래스 메서드
    @classmethod    # Decorator
    def get_population(cls):    # 클래스 변수에 접근해서 동작 수행
        print(f'현재 인스턴스의 수는 : {cls.population}입니다.')

p1 = Person('홍길동')
print(p1.name)  # 홍길동
p1.say_hello()  # 홍길동

Person.say_hello(p1)    # 홍길동 -> 이렇게 하면 되긴 되는데 굳이 쓸 필요 없음
# Person.say_hello() -> p1 이 없으면 에러
# TypeError: say_hello() missing 1 required positional argument: 'self'

Person.get_population() # 현재 인스턴스의 수는 : 1입니다.