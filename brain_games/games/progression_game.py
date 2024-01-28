import random
from brain_games.engine import run_game
from brain_games.const import MAX_PROGRESSION, MIN_PROGRESSION, PROGRESS_INSTRUCTION


def progression():
    prog = []
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    length_prog = random.randint(MIN_PROGRESSION, MAX_PROGRESSION)
    for i in range(length_prog):
        prog.append(num1 + num2 * i)

    random_index = random.randint(0, length_prog - 1)
    missed_num = prog[random_index]
    prog[random_index] = '..'
    prog_with_missed_num = ' '.join(map(str, prog))

    return prog_with_missed_num, str(missed_num)


def run_progression_game():
    run_game(progression, PROGRESS_INSTRUCTION)
