import timeit


def direct_multiplication():
    return 564654 * 24


def variable_based_multiplication():
    number_one = 564654
    number_two = 24
    return number_one * number_two


print(f"Direct: {timeit.Timer(direct_multiplication).timeit()}")
print(f"Variable: {timeit.Timer(variable_based_multiplication).timeit()}")
