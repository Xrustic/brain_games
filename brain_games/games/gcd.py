import math
from brain_games.engine import run_game
import random
from brain_games.consts import INSTRUCTION_GCD


def find_greatest_common_devisor():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    result = math.gcd(num1, num2)
    question = (f'{num1} {num2}')
    return question, str(result)


def run_gcd_game():
    run_game(find_greatest_common_devisor, INSTRUCTION_GCD)
