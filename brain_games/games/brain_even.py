#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.check_the_answer import check_the_answer
from brain_games.scripts.praise_the_winner import praise_the_winner


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answers = 0

    while 0 <= right_answers <= 2:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        guess = prompt.string('Your answer: ')
        correct = 'yes' if number % 2 == 0 else 'no'
        
        right_answers += check_the_answer(guess,correct, name)
        praise_the_winner(right_answers, name)


if __name__ == "__main__":
    main()
