import random
from os import system
from Choice import choice
def game():
    system("cls")
    diff = input("Welcome to number guesser. Enter 'E' for Easy mode, 'N' for Normal mode and 'H' for Hard mode ").upper()
    if(diff == 'E'):
        chances = 20
    elif(diff == 'N'):
        chances = 10
    elif(diff == 'H'):
        chances = 5
    else:
        print("Wrong Choice")
        return
    num = random.randint(0,101)    
    print("I am Guessing a number between 0 and 100")
    result = choice(chances,num)
    if(result[0]):
        print(f"Congrats you guessed the right number in {chances-result[1]+1} turns!!")
    else:
        print("You loose!!")
