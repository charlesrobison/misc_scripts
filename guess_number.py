# This is a guess the number game.
import random

print('Hello.  What is your name?')
name = input()

print('Hello ' + name + ', I am thinking of a number between 1 and 20.  \nPick a number:')
secretNumber = random.randint(1, 20)

