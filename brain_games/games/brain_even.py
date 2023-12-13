import prompt
import sys
import os
from random import randint
sys.path.insert(1, os.path.abspath("brain_games/scripts/"))
from welcome_user import welcome_user


def parity_check(name) -> bool:
    num = randint(1, 100)
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
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        if (parity_check(name)):
            i += 1
        else:
            return
    print('Congratulations, {0}!'.format(name))


if __name__ == '__main__':
    main()
