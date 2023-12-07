import prompt
from random import randint

i = 0


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def is_prime(num) -> bool:
    prime_num = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if num in prime_num:
        return True
    else:
        return False


def brain_prime(name: str):
    global i
    num = randint(1, 100)
    print('Question: ' + str(num))
    answer = prompt.string('Your answer: ')

    if (answer == 'yes' and is_prime(num)) or (answer == 'no' and is_prime(num) is False):
        print('Correct!')
        i += 1
    else:
        result = 'abc'
        if answer == 'yes':
            result = 'no'
        else:
            result = 'yes'
        print("'" + str(answer) + "'" + " is wrong answer ;(. Correct answer was " + "'" + result + "'" + '.')
        print("Let's try again, {0}!".format(name))
        i = 3


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while i < 3:
        brain_prime(name)
