import random
from brain_games.const import PRIME_INSTRUCTION
from brain_games.engine import run_game


def is_prime(number):
    for i in range(2, (number // 2)+1):
        if number % i == 0:
            return False
    return True


def prime_game():
    number = random.randint(1, 100)
    result = 'yes' if is_prime(number) else 'no'
    return number, result


def run_prime_game():
    run_game(prime_game, PRIME_INSTRUCTION)
