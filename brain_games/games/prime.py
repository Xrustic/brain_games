from brain_games.games.engine import run_game
from random import randint

def prime():
    num = randint(1, 100)
    prime_num = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    instruction = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = num
    if num in prime_num:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return instruction, question, right_answer

def run_prime_game():
    run_game(prime)
