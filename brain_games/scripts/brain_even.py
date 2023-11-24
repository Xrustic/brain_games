import prompt
from random import randint


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def parity_check() -> bool:
    num = randint(1, 100)

    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: ' + str(num))
    answer = prompt.string('Your answer: ')

    if (num % 2 == 0 and answer == 'yes'):
        print('Correct!')
        return True

    elif (num % 2 != 0 and answer == 'no'):
        print('Correct!')
        return True

    elif num % 2 != 0 and answer == 'yes':
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, {0}!".format(name))
        return False

    elif num % 2 == 0 and answer == 'no':
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        print("Let's try again, {0}!".format(name))
        return False


def main():
    name = welcome_user()
    i = 0
    while i < 3:
        if (parity_check()):
            i += 1
        else:
            return
    print('Congratulations, {0}!'.format(name))


if __name__ == '__main__':
    main()
