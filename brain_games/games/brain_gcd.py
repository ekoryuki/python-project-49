#!/usr/bin/env python3
import prompt
import random
import math
from brain_games.scripts.check_the_answer import check_the_answer
from brain_games.scripts.praise_the_winner import praise_the_winner


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    right_answers = 0

    while 0 <= right_answers <= 2:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)

        print(f'Question: {first_number} {second_number}')
        guess = prompt.integer('Your answer: ')
        correct = math.gcd(first_number, second_number)

        right_answers += check_the_answer(guess,correct, name)
        praise_the_winner(right_answers, name)


if __name__ == "__main__":
    main()
