import random


def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def prime_game():
    number = random.randint(1, 100)
    result = 'yes' if is_prime(number) else 'no'
    return number, result
