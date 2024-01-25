import random
from brain_games.engine import run_game
from brain_games.const import EVEN_INSTRUCTION


def is_even(number):
    return number % 2 == 0


def get_num_and_even_ans():
    number = random.randint(1, 200)
    result = 'yes' if is_even(number) else 'no'

    return number, result


def run_even_game():
    run_game(get_num_and_even_ans, EVEN_INSTRUCTION)
