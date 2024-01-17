import prompt
from brain_games.consts import ITERATIONS


def run_game(get_question_and_answer, instruction):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? \n')
    print(f'Hello, {name}!')
    print(instruction)
    for i in range(ITERATIONS):
        question, right_answer = get_question_and_answer()
        answer = prompt.string(f'Question: {question}\n'
                               'Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer. Right answer is: {right_answer}\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
