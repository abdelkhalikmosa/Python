from Dog import Dog
from Dog import Bulldog

class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

# Create instances of dogs
my_dogs = [Dog("Tom", 6), 
    Bulldog("Fletcher", 7), 
    Dog("Larry", 9)]

# Create an instance of pets
my_pets = Pets(my_dogs)

print("I have {} dogs.".format(len(my_pets.dogs)))

