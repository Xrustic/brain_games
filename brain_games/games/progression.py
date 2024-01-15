from brain_games.engine import run_game
from random import randint


def progression():
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
    question = progression.replace(number_to_hide, ' .. ').strip()
    right_answer = number_to_hide.strip()
    return question, str(right_answer)


def run_progression_game(instruction):
    run_game(progression, instruction)
