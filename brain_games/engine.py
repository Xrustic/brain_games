import prompt
from brain_games.cli import welcome_user
from brain_games.consts import ITERATIONS


def run_game(get_question_and_answer, instruction):
    name = welcome_user()
    question, right_answer = get_question_and_answer()
    print(instruction)
    i = 0
    for i in range(ITERATIONS):
        question, right_answer = get_question_and_answer()
        answer = prompt.string(f'Question: {question}\n'
                               'Your answer: ')
        if answer == right_answer:
            print('Correct!')
            i += 1
        else:
            print(f"{answer} is wrong answer. Right answer is: {right_answer}\n"
                  f"Let's try again, {name}!")
            return
    if i == ITERATIONS:
        print(f'Congratulations, {name}!')
