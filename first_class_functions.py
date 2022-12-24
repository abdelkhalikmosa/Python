from inspect import getsource


# Python functions are first class citizens
def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


def square(number):
    return number * number


# 1. assigned as a value to a variable
addition = add
print(addition)
print(getsource(addition))
print(addition(2, 3))


# 2. Passing function as an argument (callback) to another function (high order)
def calculate(first_number, second_number, function):
    return function(first_number, second_number)


print(calculate(7, 5, multiply))
print(calculate(7, 5, add))
print(calculate(7, 5, subtract))


# 3. Returned by another function
def outer():
    print('Outer')

    def inner():
        print('Inner')

    return inner  # What if inner()


myfunc = outer()
print(myfunc)
print(getsource(myfunc))
myfunc()

outer()()  # create inner function and then call it


# A nested function references and remembers a value in its enclosing scope -- closure.
def outer():
    print('Outer')
    number = 13  # free variable

    def inner():
        print('Inner')
        # number += 1 #what would happen
        print(f'The value of number is {number}')

    return inner


inner_func = outer()  # name can only be reached through the function referenced by inne
print(inner_func)
# print(getsource(inner_func))
inner_func()


def double_number(number):
    def inner():
        return number * 2

    return inner


print(double_number(2)())


def double(function):
    def inner(number):
        return function(number) * 2

    return inner


def tip(amount):
    return amount * 0.2


print(tip(10))
double_tip = double(tip)
#
print(double_tip(10))  # = print(double(tip)(10))


# Decorators
# Functions making functions
@double
def tax(amount):
    return amount * 0.1


print(tax(10))
