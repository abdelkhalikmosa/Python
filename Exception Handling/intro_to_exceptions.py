import sys

# Syntax errors vs Exceptions
# Syntax error
# The following print()) statement is syntacticly incorrect as it as an extra )
# print(5/0)) 

# Exception 
# Correcting the print () by removing the extra ) results in an exception error as division by zero is not allowed
# Python uses try and except to handle exceptions
try:
    print(5/0)
except:
    print('Division by zero is not allowed')

# The program terminates once it encounters an error (syntax or exception) and any remaining code is not going to be
# executed as long as the error is not corrected (syntax) or handeled (exception) 

print("after exception")

# Raising an exception
# Use raise to throw an exception if a condition occurs

first_name = 'Yasser'
if len(first_name) < 8:
    raise Exception('The length of the firstname should be greater than 7 letters')

print("after exception")

# The AssertionError Exception
assert('Linux' in sys.platform), "This code runs only in Linux"
