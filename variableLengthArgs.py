# The symbol * enables take in a variable number of arguments
# The variable associated with * becomes iterable 
def get_biggest_number(*args):
        return max(args)

# **kwargs in function definitions enables passing a keyworded, variable-length argument list.
# One can think of kwargs as a dictionary that maps each keyword to the value that we pass alongside it.
def full_name(**kwargs):
    for key, value in kwargs.items():
        print("{} -> {}.".format(key, value))


print("Biggest number is {} ".format(get_biggest_number(34,67,89,24,89)))
print("Biggest number is {} ".format(get_biggest_number(34,67)))
full_name(first_name="Muhammad", middle_names="Abdelkhalik Elsaid Mohamed", last_name="Mosa")