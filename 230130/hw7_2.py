class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
        
    def __del__(self):
        Doggy.num_of_dogs -= 1
        
    def bark(self):
        print(f'{self.name} : 월! 월월!')
    
    def get_status():
        print(f'birt_of_dogs : {Doggy.birth_of_dogs}\nnum_of_dogs : {Doggy.num_of_dogs}')
        
dog1 = Doggy('시바', '시바견')
dog2 = Doggy('치와', '치와와')
dog1.bark()
dog2.bark()
Doggy.get_status()
del dog1
Doggy.get_status()