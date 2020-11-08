#oop
class PlayerCharacter:
    # class object attribute
    membership = True
    age = 16

    def __init__(self, name, age):
        # if (PlayerCharacter.membership):
        #     self.name = name    #attributes
        #     self.age = age

        if (age > 18):
            self._name = name    #attributes
            self._age = age
    
    def method(self):
        print(f'my name is {self._name}')

    def speak(self):
        print(f'my name is {self._name} and i live here')

    def shout(self):
        print(f'my name is {self._name} and i am {self._age} years old!!!')

    def run(self):
        """
        This allows the player to run
        """
        print('run')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Ade', 44)
# player2 = PlayerCharacter('Tom', 16)
# player3 = PlayerCharacter.adding_things(3, 16)
# print(player1.shout())
# print(player2.run())
# print(player2.age)
# help(player1.run())
# print(player1.adding_things(3,4))

# player1.speak = 'Hello'
# print(player1.speak())








# Inheritance                       under 4pillars of OOP
class User():
    def sign_in(self):
        """
        docstring
        """
        print('logged in')

class Wizard(User):
    def funcname(self):
        """
        docstring
        """
        pass

class Archer(User):
    """
    docstring
    """
    pass

wizard1 = Wizard()
# print(wizard1.sign_in())







# Dunder methods
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }
    
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return('yess??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure())
# print(action_figure['name'])







# MRO - Method Resolution Order
# class A:
#     num = 10

# class B(A):
#     pass

# class C(A):
#     num = 1

# class D(B, C):
#     pass

# print(D.num)
# print(D.mro())


#     A
#   /   \
# /       \
# B        C
# \       /
#   \   /
#     D



class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.__mro__)
