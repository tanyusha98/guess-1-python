print("Guess the number game")
import random

def generate_number():
    return random.randint(1, 10)

print("Guess the number game")
import random

def generate_number():
    return random.randint(1, 10)

def check_guess(secret, guess):
    return secret == guess

print("Guess the number game")
secret = generate_number()
guess = int(input("Enter number 1-10: "))

if check_guess(secret, guess):
    print("You win")
else:
    print("You lose")
