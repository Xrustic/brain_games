import prompt
import sys
import os
from random import randint
sys.path.insert(1, os.path.abspath("brain_games/scripts/"))
from welcome_user import welcome_user

i = 0


def brain_gcd(name: str):
    global i
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    result = 0
    divisor = greatest_common_divisor(num1, num2)

    print('Question: ' + str(num1) + ' ' + str(num2))
    result = divisor
    answer = prompt.integer('Your answer: ')

    if (result == answer):
        print('Correct!')
        i += 1
        if i == 3:
            print('Congratulations, {0}!'.format(name))

    elif (result != answer):
        print(str(answer) + " is wrong answer ;(. "
              "Correct answer was " + str(result) + '.')
        print("Let's try again, {0}!".format(name))
        i = 3


def greatest_common_divisor(num1, num2) -> int:
    big = 0
    small = 0
    divisor = 0

    if num1 >= num2:
        big = num1
        small = num2
        divisor = small
    else:
        big = num2
        small = num1
        divisor = small

    while big % divisor != 0 or small % divisor != 0:
        divisor -= 1
    return divisor


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while i < 3:
        brain_gcd(name)


if __name__ == '__main__':
    main()
