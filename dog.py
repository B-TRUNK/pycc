#Classes Basics

class Dog:

    def __init__(self ,name ,age ,color):
        self.name   = name
        self.age    = age
        self.color  = color


    def data(self):
        print(f" Dog Name : {self.name} ,Age :  {self.age} ,Color : {self.color}")
    

pet = Dog('Caeser' ,12 ,'Paige')
pet.data()
print(pet.name)
print(pet.age)
print(pet.color)


print('\n\n')