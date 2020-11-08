from random import randint
import sys
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        # print(answer)
        guess = int(input('guess a number 1~10'))
        if 0 < guess < 11:
            if guess == answer:
                print('all good')
                break
        else:
            print('enter 1 to 10')
    except ValueError:
        print('please enter a number')
        continue