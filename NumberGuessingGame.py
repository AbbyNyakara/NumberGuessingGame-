# Import module
from random import randint

# Define global variables
HARD_LEVEL = 5
EASY_LEVEL = 10

# Let the user choose the level of difficulty
def set_difficulty():
    level = input("Choose the level of difficulty. Type 'easy' or 'hard'. ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_guess(guess, answer, turns):
    if guess > answer:
        print("Too high. ")
        return turns -1
    elif guess < answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it the answer is {answer}")

def game():
    print("Welcome to the number guessing game. ")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to make a guess.")
        guess = int(input("Make a guess. "))

        # Why do we equate the number to the function check_guess?
        turns = check_guess(guess, answer, turns)

        if turns == 0:
            print("You have run out of attempts.You lose")
            return # this return will stop the loop once you run out of attempts
        elif guess != answer:
            print("Guess again")
game()











