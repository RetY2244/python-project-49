import prompt
from brain_games import even_game
global user_name


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    print('Hello, ' + user_name + '!')


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game.the_even()


if __name__ == '__main__':
    main()
