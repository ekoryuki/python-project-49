def check_the_answer(guess, correct, name):
    match guess == correct:
        case True:
            print('Correct!')
            return +1
        case False:
            print(f"'{guess}' is wrong answer ;(. Correct answer was '{correct}'")
            print(f"Let's try again, {name}")
            return -1                                                                                                  
