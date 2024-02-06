import prompt
from brain_games.games import (calc_game, even_game, gcd_game,
                               prime_game, progression_game)

PROGRESS_INSTRUCTION = 'What number is missing in the progression?'
EVEN_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'
PRIME_INSTRUCTION = ('Answer "yes" if given number is prime. '
                     'Otherwise answer "no".')
CALC_INSTRUCTION = 'What is the result of the expression?'
GSD_INSTRUCTION = 'Find the greatest common divisor of given numbers.'
AMOUNT_OF_ROUNDS = 3


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
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def run_calc_game():
    run_game(calc_game.get_math_expression_and_result, CALC_INSTRUCTION)


def run_even_game():
    run_game(even_game.get_num_and_even_ans, EVEN_INSTRUCTION)


def run_prime_game():
    run_game(prime_game.prime_game, PRIME_INSTRUCTION)


def run_gcd_game():
    run_game(gcd_game.get_nums_pair_and_gcd, GSD_INSTRUCTION)


def run_progression_game():
    run_game(progression_game.progression, PROGRESS_INSTRUCTION)
