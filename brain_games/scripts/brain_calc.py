from brain_games.games.calc_game import get_math_expression_and_result
from brain_games.engine import run_game
from brain_games.const import CALC_INSTRUCTION


def main():
    run_game(get_math_expression_and_result, CALC_INSTRUCTION)


if __name__ == '__main__':
    main()
