from brain_games.engine import run_game
import random
from brain_games.consts import INSTRUCTION_PROGRESSION
from brain_games.consts import MIN_PROGRESSION_LENGHT, MAX_PROGRESSION_LENGHT


def get_progression_and_ans():
    start, step = random.randint(1, 100), random.randint(1, 10)
    progr = []
    for i in range(MIN_PROGRESSION_LENGHT, MAX_PROGRESSION_LENGHT):
        progr.append(start + step * i)
    missed_index = random.randint(0, len(progr) - 1)
    missed_num = progr[missed_index]
    progr[missed_index] = '..'
    progr_with_missed_num = ' '.join(map(str, progr))
    return progr_with_missed_num, str(missed_num)


def run_progression_game():
    run_game(get_progression_and_ans, INSTRUCTION_PROGRESSION)
