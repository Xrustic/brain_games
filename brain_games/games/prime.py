from brain_games.engine import run_game
from random import randint
from brain_games.consts import INSTRUCTION_PRIME


def get_prime_or_not():
    question = randint(1, 100)
    result = 'yes' if is_prime(question) else 'no'
    return question, result


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    return True if k <= 0 else False


def run_prime_game():
    run_game(get_prime_or_not, INSTRUCTION_PRIME)
