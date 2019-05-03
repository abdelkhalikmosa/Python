import sys

# Exception 
# Python uses try and except to handle exceptions
try:
    print(5/0)
except:
    print('Division by zero is not allowed')

# The program terminates once it encounters an error (syntax or exception) and any remaining code is not going to be
# executed as long as the error is not corrected (syntax) or handeled (exception) 

print(sys.platform)

# The AssertionError Exception
try:
    assert('Linux' in sys.platform), "This code runs only in Linux"
except AssertionError as e:
    print(e)


def launch_app():
    print("Simulates launching the application")


# Use the else clause to instruct Python to execute a certain block only on the absecnce of exceptions
# finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.

try:
    with open('template.yaml') as template:
        read_data = template.read()
except FileNotFoundError as e:
    print(e)
else:
    launch_app()
finally:
    print("Removing any temporary files")


"""
validates the password set by the user
"""
def set_password(user_password):
    # Raising an exception
    # Use raise to throw an exception if a condition occurs
    if len(user_password) < 10:
        raise Exception('The password should have at least 10 alphanumeric characters')
    print('password is successfully set')

try:
    set_password("123")
except:
    print('The password is less than 10 alphanumeric characters')