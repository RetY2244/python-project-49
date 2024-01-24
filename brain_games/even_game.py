from random import randint
import prompt
from brain_games.scripts.brain_even import user_name


def the_even():
    count = 0
    max_score = 3
    while count < max_score:
        random_number = randint(1, 200)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and user_answer.lower() == 'yes':
            print('Correct!')
            count = count + 1
        elif random_number % 2 != 0 and user_answer.lower() != 'no':
            return (print(user_answer + ''' is wrong answer ;(. Correct answer was 'no'.
Let's try again, ''' + user_name + '!'))
        elif random_number % 2 != 0 and user_answer.lower() == 'no':
            print('Correct!')
            count = count + 1
        elif random_number % 2 == 0 and user_answer.lower() != 'yes':
            return (print(user_answer + ''' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, ''' + user_name + '!'))
    return print('Congratulations, ' + user_name + '!')


the_even()
