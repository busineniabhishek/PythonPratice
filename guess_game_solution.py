'''# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.'''

import random

def game():
    num = random.randint(1,9)
    guess = 0
    count = 0
    while guess != num and guess != "exit":
        guess = input("Whats your guess:")

        if guess == "exit":
            break

        guess = int(guess)
        count += 1

        if guess < num:
            print("too low")
        elif guess > num:
            print("too high")
        else:
            print("Yout got it")
            print("it took you",count,"tries")



if __name__ == "__main__":
    game()