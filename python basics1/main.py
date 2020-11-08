#Fundamental data types
int, float, bool, str, list, tuple, set, dict

#Classes - custom types

#specialized data types

# None 

# int and float
print(type(2 + 4))
print(type(2 - 4))
print(type(2 / 4))
print(type(2 * 4))

print(type(2 ** 4))
print(type(2 // 4))
print(type(2 % 4))

# math fun
print(round(3.0))
print(abs(-20))     # 20

#operator precedence
# (), **, /, *, +, -
print(20 + 3 * 4)

#complex and bin(binary)
print(bin(6))
print(int('0b101', 2))

# variables
iq = 190
print(iq)

a,b,c = 1,2,3
print(a)
print(b)
print(c)

# expressions vs statements
ig = 100
# expression = '100' while statement = 'iq = 100'

# augmented assignement operator
some_value = 5
some_value = some_value + 2
# or
some_value += 2         #augmented

print(some_value)

#strings
'okay, cool'

long_string = '''
WOW
O O
---
 
'''

print(long_string)

# string concatenation
print('hi,' + ' there')

# type conversion
print(type(int(str(100))))

# escape sequences
weather = 'It\'s sunny'

# formatted strings
name = 'John'
age = 30
print('hi ' + name + '. You are ' + int(age) + ' years old')
# or
print(f'hi {name}. You are {age} years old') #recommended
# or this without variables
print('hi {}. You are {} years old'.format('Ade', '45'))
# or this without variables
print('hi {new_name}. You are {age} years old'.format(new_name='Ade', age=45))

# string indexes
test = '012345678'
print(test[6])                      #   5
#[start:stop]
print(test[0:4])                    #   123
#[start:stop:stepover]
print(test[0:8:2])                  #   0246
print(test[1:])                  #   12345678
print(test[:6])                  #   12345
print(test[::1])                  #   012345678
print(test[-3])                  #   5
print(test[::-1])                  #   876543210
print(test[::-2])                  #   86420

# immutability
test = '1234'
test = '100'
test[1] #cant work
test = test + '8'                   # 1008
test = test + str(8)
print(test)

# built-in functions and methods
quote = 'to be or not to be'
print(quote.capitalize())

#booleans
print(bool(0))                      #false
print(bool('psss'))                      #true

# exercise
birth_year = input('What year were you born?')
age = 2020 - int(birth_year)
print(f'your age is {age}')

#exercise
user = input('Username?')
password = input('password?')
pword_len = len(password)
hidden_password = '*'*pword_len
print(f'{user}, your password {hidden_password} is {pword_len} letters long')

#lists 
li = [1,2,3,4]
li2 = ['a', 'b', 'c', 'd']
li3 = [1,2,'a',True]

# lists slicing
li = ['a', 'b', 'c', 'd']
li[2] = 'p'
new_li = li[:]
new_li[0] = 'c'
print(li2[0:2])
print(li2[0::2])

# matrix
matrix = [
    [1,2,2,3],
    [5,5,7,7],
    [2,3,4,5]
]
print(matrix[0][1])

# lists method
nums = [1,2,3,4,5,6,7]
nums.append(20)
nums.insert(4,20)
#
nums.extend([100, 101, 102])
nums.pop()                  #removes the last item in the list
nums.pop(0)                  #removes the item in the list as defined
nums.remove(3)                  #removes the nth item in the list
nums.clear()                  #removes the items in the list
#
new_num = nums
print(nums)
print(new_num)

# list methods 2
nums = [1,2,3,4,5,6,7,1]
# nums.index(value, start, stop)
nums.index(2)                       # to know the position index of items
print(2 in nums)                      # to know if an item exist in an array
print(nums.count('1'))
#
new_num = nums
print(nums)
print(new_num)

# list methods 3
nums = [1,2,3,4,5,6,7,1]
nums.sort()
nums.copy()
print(sorted(nums))                         #produces a new sorted list
nums.reverse()                              #sort it first
new_num = nums
print(nums)
print(new_num)

# list pattern
nums = [1,2,3,4,5,6,7,1]
nums.sort()
nums.reverse()
print(nums[:])
print(nums)
#
print(list(range(1,100)))
print(list(range(101)))
sentence = ' '
new_sentence = sentence.join(['hi', 'i', 'am', 'kazeem'])
print(new_sentence)

#list unpacking
a,b,c,*other,d = [1,2,3,4,5,6,7]
print(a)
print(b)
print(c)
print(other)
print(d)

#   none
weapons = none
print(weapons)

#   Dictionary
dictionary = {
    'a': 1,
    'b': 2,
    'c': 'hello',
    'd': [1,2,3],
    'x': True
}
my_list = [
    {
        'a': 1,
        'b': 2,
        'c': 'hello',
        'd': [1,2,3],
        'x': True
    },
    {
        'a': 1,
        'c': 'hello',
        'd': [1,2,3],
        'x': True
    }
]
print(dictionary)
print(dictionary['b'])              # go to the key('b) and find its value
print(dictionary['d'][1])              # go to the key('b) and find its value
print(my_list[0]['d'][2])

# dictionary keys
dictionary = {
    123: [1,2,3],
    True: 'hello',
    [100]: True,
    '[256]': False,
    '[256]': 'hello'
}
print(dictionary('[256]'))

# dictionary method
user = {
    123: [1,2,3],
    'greet': 'hello',
    '[256]': 'hello',
    'age': 123
},
user2 = dict(name='john')
print(user2)
print(user.get('age'))
print(user.get('age', 30))              #giving age a default value 30 incase it doesnt exist

# dictionary method 2
user = {
    123: [1,2,3],
    'greet': 'hello',
    '[256]': 'hello',
    'age': 123
}
print('day' in user)                                    #returns true or false
print('day' in user.keys())
print('age' in user.keys())
print('hello' in user.values())
print(user.items())                                     #to gra all items in a dict
print(user.pop('age'))
print(user.popitem('age'))
print(user.update({'age':69}))
print(user.update({'ages':70}))
#
user2 = user.copy()
print(user.clear())
print(user2)

#Tuples
my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)
#
user = {
    (1,2): [1,2,3],
    'greet': 'hello',
    '[256]': 'hello',
    'age': 123
}
print(user.items())                 #returns in tuples
print(user[(1,2)])

#Tuples 2
my_tuple = (1,2,3,4,5,5)
new_tuple = my_tuple[1:2]
x,y,z,*other = (1,2,3,4,5)
print(new_tuple)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

#sets
my_list = [1,2,3,4,5,5,5,6,7,8]
print(set(my_list))
my_set = {1,2,3,4,5,5,6,7,8}
my_set.add(100)
my_set.add(2)
print(my_set)                                   #doesnt return a duplicate
print(len(my_set))
print(list(my_set))
#
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

#sets 2
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10,11}
#
print(my_set.difference(your_set))
print(my_set.discard(5))                        # print(my_set)
print(my_set.difference_update(your_set))       #print(my_set)
print(my_set.intersection(your_set))         #or         print(my_set & your_set)) 
print(my_set.isdisjoint(your_set))
print(my_set.union(your_set))                #or         print(my_set | your_set)) 
print(my_set.issubset(your_set))            #   returns true or false
print(your_set.issuperset(my_set))            #   returns true or false

