from brain_games.engine import run_game
from random import randint


def prime():
    question = randint(1, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return question, right_answer


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    return True if k <= 0 else False


def run_prime_game(instruction):
    run_game(prime, instruction)
