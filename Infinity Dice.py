print ("| Infinity Dice Game |")

def dice():
    import random
    maxRoll= int(input("How many Slides: "))
    roll=random.randint(0,maxRoll)
    print("You rolled:",roll)
    rollAgain=input("Roll again (y/n): ")
    if rollAgain =="y":
        dice()
    elif rollAgain =="n":
        print ("| Game Over: Thank you for playing")
        exit
    else:
        print ("Invalid entry")

print (dice())