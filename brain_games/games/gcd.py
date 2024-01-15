import math
from brain_games.engine import run_game
from random import randint


def find_greatest_common_devisor():
    num1, num2 = randint(1, 100), randint(1, 100)
    right_answer = math.gcd(num1, num2)
    question = str(num1) + ' ' + str(num2)
    return question, str(right_answer)


def run_gcd_game(instruction):
    run_game(find_greatest_common_devisor, instruction)
