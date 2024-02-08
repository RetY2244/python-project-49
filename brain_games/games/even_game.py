import random

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    return question % 2 == 0


def get_questions_and_answer():
    question = random.randint(1, 200)
    answer = 'yes' if is_even(question) else 'no'

    return question, answer
