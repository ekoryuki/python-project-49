def check_the_answer(guess, corr, name):
    match guess == corr:
        case True:
            print('Correct!')
            return +1
        case False:
            print(f"'{guess}' is wrong answer ;(. Correct answer was '{corr}'")
            print(f"Let's try again, {name}")
            return -1
