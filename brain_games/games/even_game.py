import random


def is_even(number):
    return number % 2 == 0


def get_num_and_even_ans():
    number = random.randint(1, 200)
    result = 'yes' if is_even(number) else 'no'

    return number, result
