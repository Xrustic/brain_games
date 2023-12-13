import prompt
from random import randint
import sys
sys.path.insert(1, '/home/olga/Projects/python-project-49/brain_games/scripts/')
from welcome_user import welcome_user

i = 0


def brain_progression(name: str):
    global i
    num = randint(1, 100)
    number_of_elements = randint(5, 10)
    step = randint(1, 10)
    counter = 1

    index = randint(0, number_of_elements - 1)
    numbers = (num, )
    progression = ' ' + str(num) + ' '
    while counter < number_of_elements:
        num += step
        progression += str(num) + ' '
        numbers += (num, )
        counter += 1

    number_to_hide = ' ' + str(numbers[index]) + ' '
    progression = progression.replace(number_to_hide, ' .. ').strip()

    print('Question: ' + progression)
    result = number_to_hide.strip()
    answer = prompt.string('Your answer: ')

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


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    while i < 3:
        brain_progression(name)


if __name__ == '__main__':
    main()
