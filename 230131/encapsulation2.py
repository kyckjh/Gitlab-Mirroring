class Person:
    def __init__(self, age):
        self.__age = age
    
    @property
    def age2(self):
        return self.__age
        
    @age2.setter
    def age3(self, age):
        if age < 20:
            raise ValueError('너무 어린데?')
        else:
            self.__age = age
            
    @age2.deleter
    def age4(self):
        del self.__age
        
    
kimssafy = Person(20)
print(f'kimssafy는 {kimssafy.age2}이다')

kimssafy.age3 = 24
print(f'kimssafy는 {kimssafy.age2}이다')

del kimssafy.age4

try:
    print(f'kimssafy는 {kimssafy.age2}이다')
except AttributeError:
    print('AttributeError Occured')
