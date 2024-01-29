import prompt
from brain_games.const import AMOUNT_OF_ROUNDS


def run_game(get_questions_and_answer, instruction):
    name = prompt.string("Welcome to the Brain Games!\n"
                         "May I have your name? ")
    print(f"Hello, {name}!\n"
          f"{instruction}")
    for _ in range(AMOUNT_OF_ROUNDS):
        question, answer = get_questions_and_answer()

        user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"'{user_answer}') is wrong answer ;(."
                  f" Correct answer is '{answer}'.\n"
                  f"Let's try again, {name}")
            return
    print(f'Congratulations, {name}!')
