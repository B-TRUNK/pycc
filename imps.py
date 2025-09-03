from dog import *

pet = Dog('Caeser' ,12 ,'Paige')
pet.data()
pet.get_breed()

pet.breed = 'Carnivore'
pet.get_breed()
pet.breed_modify('Herbivore')
pet.get_breed()


print('\n\n')