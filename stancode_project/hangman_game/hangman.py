"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


ANS = random_word()


def main():
    cur_ans = initialize_ans(ANS)
    N_TURNS = 7
    while N_TURNS > 0:
        print("")
        graph(N_TURNS)
        print('The word looks like: ' + cur_ans)
        print('You have ' + str(N_TURNS) + ' guesses left.')
        cur_guess = input('Your guess: ')
        cur_guess = cur_guess.upper()

        if not cur_guess.isalpha() or len(cur_guess) > 1:  # when user's input is illegal
            print('illegal format.')
        else:
            if cur_guess in ANS:  # when user's input is in answer
                if cur_guess not in cur_ans:  # first guess
                    cur_ans = build_new_ans(cur_ans, cur_guess)
                    print('You are correct!')
                    if cur_ans == ANS:  # check whether guess the answer or not
                        print('You win!!')
                        break
            else:  # when user's input is not in answer
                print("There is no " + cur_guess + "'s in the word.")
                N_TURNS = N_TURNS - 1

    if N_TURNS == 0:  # deal with OBOB problem
        graph(N_TURNS)
        print('You are completely hung :(')

    print('The word was: ' + ANS)


def initialize_ans(target):
    """
    :param target: str, the answer defined by randomized function
    """
    word = str()
    for i in range(len(target)):
        word = word + "-"
    return word


def build_new_ans(cur_ans, cur_guess):
    """
    :param cur_ans: str, the current answer
    :param cur_guess: str, the current guess
    """
    new_ans = ""
    for i in range(len(ANS)):
        if ANS[i] == cur_guess:
            new_ans = new_ans + cur_guess
        else:
            new_ans = new_ans + cur_ans[i]
    return new_ans


def graph(n):
    """
    :param n: int, current life count
    """
    if n == 7:
        print('|----|\n|\n|\n|\n|\n===========')
    if n == 6:
        print('|----|\n|    O\n|\n|\n|\n===========')
    if n == 5:
        print('|----|\n|    O\n|    |\n|\n|\n===========')
    if n == 4:
        print('|----|\n|    O\n|  --|\n|\n|\n===========')
    if n == 3:
        print('|----|\n|    O\n|  --|--\n|\n|\n===========')
    if n == 2:
        print('|----|\n|    O\n|  --|--\n|  _/\n|\n===========')
    if n == 1:
        print('|----|\n|    O\n|  --|--\n|  _/-\_\n|\n===========')
    if n == 0:
        print('|----|\n|    Q\n|  --|--\n|  _/-\_\n|  R.I.P.\n===========')


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
