def methodcaption(another):
    """
    docstring
    """
    return another()

def add_two_numbers():
    """
    docstring
    """
    return 35 + 77

# print(methodcaption(add_two_numbers))
# print(methodcaption(lambda: 35 + 77))

my_list = [23, 34, 21, 45, 56]
# print(list(filter(lambda x: x != 13, my_list)))

# or

# def not_thirteen(x):
#     return x != 13

# print(list(filter(not_thirteen, my_list)))

# or

# list comprehension
print([x for x in my_list if x != 35])