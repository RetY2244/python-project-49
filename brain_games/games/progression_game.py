import random

INSTRUCTION = 'What number is missing in the progression?'


MAX_PROGRESSION = 10
MIN_PROGRESSION = 5


def get_questions_and_answer():
    prog = []
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    length_prog = random.randint(MIN_PROGRESSION, MAX_PROGRESSION)
    for i in range(length_prog):
        prog.append(num1 + num2 * i)

    random_index = random.randint(0, length_prog - 1)
    answer = prog[random_index]
    prog[random_index] = '..'
    question = ' '.join(map(str, prog))

    return question, str(answer)
