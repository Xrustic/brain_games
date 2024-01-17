from brain_games.engine import run_game
import random
from brain_games.consts import INSTRUCTION_PROGRESSION


def get_progression():
    num = random.randint(1, 100)
    number_of_elements = random.randint(5, 10)
    step = random.randint(1, 10)
    counter = 1

    index = random.randint(0, number_of_elements - 1)
    numbers = (num, )
    progression = ' ' + str(num) + ' '
    while counter < number_of_elements:
        num += step
        progression += str(num) + ' '
        numbers += (num, )
        counter += 1

    number_to_hide = ' ' + str(numbers[index]) + ' '
    question = progression.replace(number_to_hide, ' .. ').strip()
    result = number_to_hide.strip()
    return question, str(result)


def run_progression_game():
    run_game(get_progression, INSTRUCTION_PROGRESSION)
