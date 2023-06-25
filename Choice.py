def choice(chances,num):
    if(chances==0):
        return([False,chances])
    guess = int(input(f"You have {chances} chance(s) left\nEnter your guess: "))
    if(guess == num):
        return([True,chances])
    elif(guess<num):
        if(guess<num-10):
            print("Too low")
        else:
            print("Little low")
    elif(guess>num):
        if(guess>num+10):
            print("Too high")
        else:
                print("Little high")
    return choice(chances-1,num)
