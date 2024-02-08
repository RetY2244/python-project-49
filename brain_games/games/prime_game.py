import random


INSTRUCTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')


def is_prime(question):
    for i in range(2, (question // 2) + 1):
        if question % i == 0:
            return False
    return True


def get_questions_and_answer():
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
