from brain_games.games.engine import run_game
from random import randint

def calc():
    x = randint(1, 10)
    y = randint(1, 10)
    expression = randint(0, 2)
    instruction = 'What is the result of the expression?'
    if expression == 0:
        question = str(str(x) + '+' + str(y))
        right_answer = x + y
    elif expression == 1:
        question = str(str(x) + '-' + str(y))
        right_answer = x - y
    else:
        question = str(str(x) + '*' + str(y))
        right_answer = x * y
    return instruction, question, right_answer


def run_calc_game():
    run_game(calc)
