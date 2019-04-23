''' 
Credit: This OOP tutorial is based on the ones in 
https://realpython.com/python3-object-oriented-programming/
'''

class Dog:
    # Class attributes
    species = 'mammal'

    # Initializer for instance atrributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance methods
    # Decribes each dog
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return("{} says {}".format(self.name, sound))

# Inheritance
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# get the maximum number
# The symbol * enables take in a variable number of arguments
# The variable associated with * becomes iterable 
def get_biggest_number(*args):
        return max(args)

# Instantiating dog objects
molly = Dog('Molly', 3)
charlie = Dog('Charlie', 5)
daisy = Dog('Daisy', 4)
jim = Bulldog("Jim", 8)

# Calling instance methods
print(daisy.description())
print(daisy.speak("Gruff Gruff"))
# Objects from a child class can access methods from parent class
print(jim.description())
# Theu can also access their own methods define din the child class
print(jim.run("slowly"))

print("{} is {} years old, and {} is {}.".format(molly.name, molly.age, daisy.name, daisy.age))
print("The oldest dog is {} years old.".format(max(molly.age, charlie.age, daisy.age)))

# is instance?
print(isinstance(jim, Dog))
print(isinstance(jim, Bulldog))
print(isinstance(molly, Bulldog))
print(isinstance(molly, Dog))

