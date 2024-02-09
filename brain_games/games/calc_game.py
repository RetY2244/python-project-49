import random

INSTRUCTION = 'What is the result of the expression?'


MATH_SIGNS = ['+', '-', '*']


def get_questions_and_answer():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_sign = random.choice(MATH_SIGNS)
    question = f'{str(num1)} {math_sign} {str(num2)}'
    if math_sign == '+':
        answer = num1 + num2
    elif math_sign == '-':
        answer = num1 - num2
    elif math_sign == '*':
        answer = num1 * num2
    return question, str(answer)
