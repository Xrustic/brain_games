from brain_games.games.engine import run_game
from random import randint


def progression():
    num = randint(1, 100)
    number_of_elements = randint(5, 10)
    step = randint(1, 10)
    counter = 1
    instruction = 'What number is missing in the progression?'

    index = randint(0, number_of_elements - 1)
    numbers = (num, )
    progression = str(num) + ' '
    while counter < number_of_elements:
        num += step
        progression += str(num) + ' '
        numbers += (num, )
        counter += 1

    number_to_hide = str(numbers[index])
    progression = progression.replace(number_to_hide, '..')
    question = progression
    right_answer = number_to_hide
    return instruction, question, right_answer


def run_progression_game():
    run_game(progression)
