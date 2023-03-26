"""
Guess a number from 1 to 10
secret_number=
user_number

Enter a number to guess = 6

You have guessed it right.

Oh no! You guessed it wrong, the number was 5
"""
import random

secret_number=random.randint(1,10)
user_number=int(input("Guess a number = "))

if secret_number==user_number:
    print("You won")
else:
    print(f"Oh no! The number was {secret_number}")