from brain_games.engine import run_game
import random
from brain_games.consts import INSTRUCTION_EVEN


def get_num_and_even_ans():
    question = random.randint(1, 100)
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result


def run_even_game():
    run_game(get_num_and_even_ans, INSTRUCTION_EVEN)
