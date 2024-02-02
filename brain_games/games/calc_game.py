import random
from brain_games.const import MATH_SIGNS


def get_math_expression_and_result():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_sign = random.choice(MATH_SIGNS)
    expression = f'{str(num1)} {math_sign} {str(num2)}'
    result = 0
    if math_sign == '+':
        result = num1 + num2
    elif math_sign == '-':
        result = num1 - num2
    elif math_sign == '*':
        result = num1 * num2
    return expression, str(result)
