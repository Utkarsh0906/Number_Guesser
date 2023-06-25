from Game import game
game()
while(True):
    if(input("Enter 'Y' to Restart or 'N' to Stop playing").upper() == 'Y'):
        game()
    else:
        break