# def hello():
#     return 'heelllloooooo'

# greet = hello()
# del greet
# print(hello())


# # Higher Order Function
# def play(func):
#     return func()

# def run():
#     print('running now')

# a = play(run)
# print(a)


# decorator
# def my_decorator(func):
#     def wrap_func():
#         print('************')
#         func()
#         print('************')
#     return wrap_func

# @my_decorator
# def hello():
#     return print('helllllooooo')

# @my_decorator
# def bye():
#     return print('see ya later')

# hello()
# bye()


# why decorators
# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper

# @performance
# def long_time():
#     for i in range(100000000):
#         i*5

# long_time()








# Error handling
# while True:
#     try:
#         age = int(input('What is your age?'))
#         10/age
#     except ValueError:
#         print('Please enter a number')
#     except ZeroDivisionError:
#         print('Please enter age higher than zero')
#     else:
#         print('thank you!')
#         break
#     finally:
#         print('ok, i am finally done')

# Error handling 2
# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(f'Please enter number {err}')

# print(sum('1', 3))


# Error handling 3 - customizing your own error
# while True:
#     try:
#         age = int(input('What is your age?'))
#         10/age
#        raise ValueError('this is a value error')
#     except ZeroDivisionError:
#         print('Please enter age higher than zero')
#     else:
#         print('thank you!')
#     finally:
#         print('ok, i am finally done')
#         print('hello there')