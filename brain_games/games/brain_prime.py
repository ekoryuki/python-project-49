#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.check_the_answer import check_the_answer
from brain_games.scripts.praise_the_winner import praise_the_winner


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answers = 0

    while 0 <= right_answers <= 2:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        guess = prompt.string('Your answer: ')
        correct = 'yes' if check_primality(number) else 'no'

        right_answers += check_the_answer(guess, correct, name)
        praise_the_winner(right_answers, name)


def check_primality(number):
    flag = True
    for i in range(2, number // 2):
        if number % i == 0:
            flag = False
            break
    return flag


if __name__ == "__main__":
    main()
