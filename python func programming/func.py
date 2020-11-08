# pure functions    /   has no side effects(no connection with the outside world)
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by2([1,2,3]))





#map, filter, zip, reduce
#map
# my_list = [1,2,3,4]
# def multiply_by2(item):
#     return item*2
# print(list(map(multiply_by2, my_list)))

#filter
# my_list = [1,2,3,4,5]
# def only_odd(item):
#     """
#     checks for only odd numbers
#     """
#     return item % 2 != 0
# print(list(filter(only_odd, my_list)))

#zip
# my_list = [1,2,3,4,5]
# your_list = [10,20,30,40,50, 60]
# print(list(zip(my_list, your_list)))

#reduce
# from functools import reduce
# my_list = [1,2,3,4,5]
# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item
# print(reduce(accumulator,my_list,0))


# lambda expressions
# my_list = [1,2,3,4]
# print(list(map(lambda item: item*2, my_list)))
# print(list(filter(lambda item: item % 2 != 0, my_list)))
# from functools import reduce
# print(reduce(lambda acc, item: acc+item, my_list))

# exercise
# my_list = [1,2,3,4]
# print(list(map(lambda item: item**2, my_list)))

# list sorting
# a = [(0,2), (4,3), (9,9), (10, -1)]
# a.sort(key=lambda x: x[1])
# print(a)


# list, set, dictionary comprehension
# my_list = [param for param in 'hello']
# my_list2 = [num for num in range(0,100)]
# my_list3 = [num*2 for num in range(0,100)]
# my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)

# set comprehension
my_set = {param for param in 'hello'}
my_sett2 = {num for num in range(0,100)}
my_set3 = {num*2 for num in range(0,100)}
my_set4 = {num**2 for num in range(0,100) if num % 2 == 0}
print(my_set)
# print(my_set2)
# print(my_set3)
# print(my_set4)


# dict comprehension
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2 == 0}
my_dict2 = {num:num*2 for num in [1,2,3]}
# print(my_dict)
# print(my_dict2)


# exercise
some_list = ['a','b','c','d','e','f','f','f','g','g','g','h','i']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)