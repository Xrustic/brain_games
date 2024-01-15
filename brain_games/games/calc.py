from brain_games.engine import run_game
import random
from random import randint


def calculation():
    num1, num2 = randint(1, 100), randint(1, 100)
    mylist = ['+', '-', '*']
    expression = random.choice(mylist)
    question = str(num1) + ' ' + expression + ' ' + str(num2)
    right_answer = eval(question)
    return question, str(right_answer)


def run_calc_game(instruction):
    run_game(calculation, instruction)
