import prompt
from random import randint

i = 0
name = ''


def welcome_user() -> str:
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def brain_calc(options):
    global i
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    result = 0

    if options == 0:
        print('Question: ' + str(num1) + '+' + str(num2))
        result = num1 + num2

    elif options == 1:
        print('Question: ' + str(num1) + '-' + str(num2))
        result = num1 - num2

    elif options == 2:
        print('Question: ' + str(num1) + '*' + str(num2))
        result = num1 * num2
    answer = prompt.integer('Your answer: ')

    if (result == answer):
        print('Correct!')
        i += 1

    elif (result != answer):
        print(str(answer) + " is wrong answer ;(. Correct answer was " + str(result) + '.')
        print("Let's try again, {0}!".format(name))
        i = 3


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    while i < 3:
        brain_calc(randint(0, 2))
