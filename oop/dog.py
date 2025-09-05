#Classes Basics

class Dog:


    def __init__(self ,name ,age ,color):
        self.name   = name
        self.age    = age
        self.color  = color
        self.breed  = 'Kind'


    def data(self):
        print(f" Dog Name : {self.name} ,Age :  {self.age} ,Color : {self.color}")
    
    def get_breed(self):
        print(f"This Dog is :  {self.breed}") 


    #Modifying an Attribute’s Value Through a Method
    def breed_modify(self ,the_breed):
        self.breed = the_breed