import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


def parity_check():
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        num = randint(1, 100)
        print('Question: ' + str(num))
        answer = prompt.string('Your answer: ')
        if (num % 2 == 0 and answer == 'yes') or (num % 2 != 0 and answer == 'no'):
            print('Correct!')
            i += 1
        elif num % 2 != 0 and answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, {0}!".format(name))
            return 0
        elif num % 2 == 0 and answer == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print("Let's try again, {0}!".format(name))
            return 0
