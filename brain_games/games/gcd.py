import math
from brain_games.engine import run_game
from random import randint
from brain_games.consts import INSTRUCTION_GCD


def find_greatest_common_devisor():
    num1, num2 = randint(1, 100), randint(1, 100)
    result = math.gcd(num1, num2)
    question = str(num1) + ' ' + str(num2)
    return question, str(result)


def run_gcd_game():
    run_game(find_greatest_common_devisor, INSTRUCTION_GCD)
