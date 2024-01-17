from brain_games.engine import run_game
import random
from brain_games.consts import INSTRUCTION_CALC, MATH_SIGNS


def get_math_expression_and_res():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_sign = random.choice(MATH_SIGNS)
    question = (f'{num1} {math_sign} {num2}')
    result = eval(question)
    return question, str(result)


def run_calc_game():
    run_game(get_math_expression_and_res, INSTRUCTION_CALC)
