from brain_games.games.engine import run_game
from random import randint


def gcd():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    right_answer = greatest_common_divisor(num1, num2)
    instruction = 'Find the greatest common divisor of given numbers.'
    question = str(num1) + ' ' + str(num2)
    return instruction, question, right_answer


def greatest_common_divisor(num1, num2) -> int:
    big = 0
    small = 0
    divisor = 0

    if num1 >= num2:
        big = num1
        small = num2
        divisor = small
    else:
        big = num2
        small = num1
        divisor = small

    while big % divisor != 0 or small % divisor != 0:
        divisor -= 1
    return divisor


def run_gcd_game():
    run_game(gcd)
