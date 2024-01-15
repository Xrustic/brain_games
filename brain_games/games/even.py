from brain_games.engine import run_game
from random import randint


def even_or_not():
    question = randint(1, 100)
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return question, right_answer


def run_even_game(instruction):
    run_game(even_or_not, instruction)
