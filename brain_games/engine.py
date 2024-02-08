import prompt

AMOUNT_OF_ROUNDS = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def run_game(game):
    name = welcome_user()
    print(game.INSTRUCTION)

    for _ in range(AMOUNT_OF_ROUNDS):
        question, answer = game.get_questions_and_answer()
        user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"'{user_answer}') is wrong answer ;(."
                  f" Correct answer is '{answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
