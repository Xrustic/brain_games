import prompt
from brain_games.cli import welcome_user


def run_game(get_question_and_answer):
    name = welcome_user()
    instruction, question, right_answer = get_question_and_answer()
    print(instruction)
    i = 0
    while i < 3:
        instruction, question, right_answer = get_question_and_answer()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if str(answer) == str(right_answer):
            print('Correct!')
            i += 1
        else:
            print(answer + ' is wrong answer. Right answer is: '
                  + str(right_answer))
            print(f"Let's try again, {name}!")
            return
    if i == 3:
        print(f'Congratulations, {name}!')
