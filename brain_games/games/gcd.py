from brain_games.games.engine import run_game
from random import randint

def gcd():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    instruction = 'Find the greatest common divisor of given numbers.'
    question = str(num1) + ' ' + str(num2)
    if num1 >= num2:
        right_answer = num1
    else:
        right_answer = num2
    return instruction, question, right_answer


def run_gcd_game():
    run_game(gcd)
