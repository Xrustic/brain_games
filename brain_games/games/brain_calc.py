import prompt
from random import randint
import sys
sys.path.insert(1, '/home/olga/Projects/python-project-49/brain_games/scripts/')
from welcome_user import welcome_user

i = 0
result = 0


def brain_calc(options, name: str):
    global i
    global result
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    if options == 0:
        addition(num1, num2)

    else:
        substraction(num1, num2) if options == 1 else multi(num1, num2)

    answer = prompt.integer('Your answer: ')

    correct(name) if result == answer else wrong(answer, result, name)


def multi(num1, num2):
    global result
    print('Question: ' + str(num1) + ' * ' + str(num2))
    result = num1 * num2


def substraction(num1, num2):
    global result
    print('Question: ' + str(num1) + ' - ' + str(num2))
    result = num1 - num2


def addition(num1, num2):
    global result
    print('Question: ' + str(num1) + ' + ' + str(num2))
    result = num1 + num2


def wrong(answer, result, name: str):
    global i
    print(str(answer) + " is wrong answer ;(. "
          "Correct answer was " + str(result) + '.')
    print("Let's try again, {0}!".format(name))
    i = 3


def correct(name: str):
    global i
    print('Correct!')
    i += 1
    if i == 3:
        print('Congratulations, {0}!'.format(name))


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    while i < 3:
        brain_calc(randint(0, 2), name)


if __name__ == '__main__':
    main()
