import prompt
from random import randint

i = 0


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


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
