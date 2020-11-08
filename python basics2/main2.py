#conditional logics
is_old = True
is_licensed = True
if is_old and is_licensed:
    print('You are old enough to drive and you can drive now!')
else:
    print('You are young to drive!')

#truthy and falsy
username = 'John'
password = '123456'
if username and password:
    print('You are now signed in!')
else:
    print('incorrect password!')

#ternery operator/conditional expression
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

#short circuiting
is_friend = True
is_user = True
print(is_friend and is_user)
if is_friend and is_user:
    print('best friends forever')                               #false
    #
if is_friend or is_user:                                       #true
    print('best friends forever')

#logical operators
# >, <, =, ==, <=, >=, !=, and, or, not
print(not(True))

#Exercise
is_magician = True
is_expert = True
#check if magician and expert
#check if magician but not expert
#if you're a magician
if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('at least you\'re getting there')
elif not is_magician:
    print('you need magic powers')

# is vs ==
print(True == True)
print('1' == 1)
print([] == 1)
print(10 == 10.0)
print([1,2,3] == [1,2,3,4])
#
print(True is True)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([1,2,3] is [1,2,3,4])

#loops
for item in 'This is python':
    print(item)
for item in [1,2,3,4,5,6]:              #list
    print(item)
for item in {1,2,3,4,5,6}:              #set
    print(item)
for item in (1,2,3,4,5,6):              #tuple
    print(item)
for item in (1,2,3,4,5,6):              #1a, 1b, 1c, 2a, 2b, etc
    for x in [a,b,c]:
        print(item, x)

#iterables
is_user = {
    'name': 'Doe',
    'age': 59,
    'can_swim': False
}
for item in is_user.items():
    print(item)
for item in is_user.values():
    print(item)
for item in is_user.keys():
    print(item)
#
for item in is_user.items():
    key, value = item
    print(key, value)
for key, value in is_user.items():
    print(key, value)
for k, v in is_user.items():
    print(k, v)
#Nouns: iterable - list, dictionary, tuple, set, string
#Actions: iterate - one by one checking of each item in the collection

#exercise
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
  counter = counter + item
print(counter)                                      #55 total sum of items in the list

# range()
for number in (range(0, 10, 2)):
    print(number)
for number in (range(10, 0, -2)):
    print(number)
for number in (range(10, 0, -2)):
    print(list(range(10)))
for number in (range(2)):
    print(list(range(10)))

#enumerate()
for i,char in enumerate('Heeeelllllooooo'):
    print(i,char)
for i,char in enumerate([1,2,3,4,5,6]):
    print(i,char)
for i,char in enumerate((1,2,3,4,5,6)):
    print(i,char)

#exercise
for i,char in enumerate(list(range(100))):
    # print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')

#while loops
i=0
while i < 10:
    print(i)
    i += 1
    # break
else:
    print('Done with all the works')

# while loops 2
my_list = [1,2,3,4,5,6]
for item in my_list:
    print(item)
#
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break
#
while True:
    response = input('Say something:')
    if (response == 'bye'):
        break

# break, continue, pass
my_list = [1,2,3,4,5,6]
for item in my_list:
    #thinking about it
    pass
for item in my_list:
    print(item)
    continue
i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass

# GUI
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
# iterate over picture
    # if 0 -> print ''
    # if 1 -> print *
fill = '$'
empty = ' '
for image in picture:
    for pixel in image:
        if pixel:
            print(fill, end='')
            print(fill, end='')
            print(fill, end='')
            print(fill, end='')
        else:
            print(empty, end='')
            print(empty, end='')
            print(empty, end='')
            print(empty, end='')
    print('')

#exercise find duplicates
some_list = [a,b,c,d,d,g,gg,hh,f,d,eee,g,ghh,h,t,eed,ff,ff,ss,sf,fg]
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

# functions
def say_helloo():
    print('hellllooooo')
say_hello()

# Parameter/default parameter
def say_hello(name='Dayo D1', emoji='lol'):
    print(f'hellllooooo {name}{emoji}')
say_hello()

# argument which are the values passed to a parameter
say_hello('kazeem', 'lol')
say_hello('Bola', 'lol')

# positional arg
say_hello('lol', 'kazeem')

# keyword arguments
say_hello(emoji='lol',name="bibi")

# return
def sum(num1, num2):
    return num1 + num2 
sum(4,5)

# Methods & functions
'hello'.capitalize()

# Docstrings
def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)
test('!!!')
#
help(test)
print(test.__doc__)

# clean code
def is_even(num):
    return num % 2 == 0
print(is_even(50))

# *arg and *keyword args
def super_fun(*args):
    print(*args)
    return sum(args)
print(super_fun(1,2,3,4,5))
#**kwargs
def super_fun(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_fun(1,2,3,4,5, num1=5, num2=10))
#Rule: params, *args, default parameters, **kwargs

#exercise
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)
print(highest_even([2,19,2,3,4,8,11]))

#scope - what variables do i have access to 
if True:
    x = 10
def some_func():
    total = 100
    print(x)

#Scope rules
#1 - start with local
#2 - parent local
#3 - Global
#4 - built in python functions
a = 1
def parent():
    a = 10
    def confusion():
        return a
    return confusion()
print(parent())
print(a)

#global keyword
total = 0
def count(total):
    total += 1
    return total
print(count(count(count(total))))

#nonlocal
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

