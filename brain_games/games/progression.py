from brain_games.engine import run_game
import random
from brain_games.consts import INSTRUCTION_PROGRESSION


def get_progression_and_ans():
    num, step = random.randint(1, 100), random.randint(1, 10)
    progr = [num]
    for i in range(random.randint(5, 10)):
        progr.append(progr[-1] + step)
    right_answer = ' ' + str(progr[random.randint(0, len(progr) - 1)]) + ' '
    progr_str = str(progr)
    progr_str = ' ' + progr_str + ' '
    progr_str = progr_str.replace(',', '').replace('[', '').replace(']', '')
    progr_str = progr_str.replace(right_answer, ' .. ').strip()
    right_answer = right_answer.strip()
    return progr_str, right_answer


def run_progression_game():
    run_game(get_progression_and_ans, INSTRUCTION_PROGRESSION)
