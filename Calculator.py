#welcome
#hi
import random
name = input("pls enter your name:")
print("hi " + name)
print("welcome to random number game!!")
number = random.randint(1, 101)
print("enter your guess between 1-100: ")
guess = 0

while guess != number:
    guess = int(input())
       
       
    if guess < number:
        print("too low!!")
    elif guess > number:
        print("too high!!")
    else:
        print("you won the game")
