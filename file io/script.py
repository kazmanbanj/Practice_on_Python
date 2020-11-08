# my_file = open('test.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# print(my_file.readlines())
# my_file.close()







# Standard way to Read, write, append in python

# with open('test.txt', mode='r+') as my_file:
#     print(my_file.readlines())

# with open('test.txt', mode='r+') as my_file:
#     text = my_file.write(':)')
#     print(text)

# with open('test.txt', mode='a') as my_file:
#     text = my_file.write('\nthis will append to the text file with the mode a')
#     print(text)

# with open('testAnother.txt', mode='w') as my_file:
#     text = my_file.write('\nthis will create a new text file with the mode w')
#     print(text)









# file paths
try:
    with open('movedHere/testAnother.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
except IOError as err:
    print('IO error')