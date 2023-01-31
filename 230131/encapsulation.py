class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
        
    @age.setter
    def age(self, age):
        if age < 20:
            raise ValueError('너무 어린데?')
        else:
            self._age = age
            
kimssafy = Person(20)
print(f'kimssafy는 {kimssafy.age}이다')

kimssafy.age = 24
print(f'kimssafy는 {kimssafy.age}이다')