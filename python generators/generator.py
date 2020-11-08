# list is an iterable
# range is a generator (a subset of an iterable)

# list
# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
# 
# my_list = make_list(100)
# print(my_list)




# generator
# def generate_func(num):
#     for i in range(num):
#         yield i

# for item in  generate_func(1000):
#     print(item)


# comparing generator(range) with iterable(list)
# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper
# # most favourable
# @performance
# def long_time():
#     print('1')
#     for i in range(100000000):
#         i*5
# # unfavourable
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(100000000)):
#         i*5

# long_time()
# long_time2()




# Fibonacci
def fib(number):
    a=0
    b=1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(21):
    print(x)