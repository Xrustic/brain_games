from brain_games.games.engine import run_game
from random import randint

def get_question_and_answer():
    num = randint(1, 100)
    instruction = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = num
    if num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return instruction, question, right_answer

def run_even_game():
    run_game(get_question_and_answer)
