#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.check_the_answer import check_the_answer
from brain_games.scripts.praise_the_winner import praise_the_winner


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    right_answers = 0

    while 0 <= right_answers <= 2:
        start = random.randint(0, 1000)
        step = random.randint(1, 20)
        progression = []
        for i in range(1, 11):
            progression.append(start + i * step)

        index_of_hidden_integer = random.randint(0, 9)
        correct = progression[index_of_hidden_integer]
        progression[index_of_hidden_integer] = "..."
        print(f'Question: {progression}')
        guess = prompt.integer('Your answer: ')

        right_answers += check_the_answer(guess,correct, name)
        praise_the_winner(right_answers, name)


if __name__ == "__main__":
    main()
