import random
print ("Guess The Number")
print (""" In this game you get to guess the correct number.
       The game will guide you, if your guess is:
       1- low.
       2- High.""")
print()
print ("Ready... Steady ... Go Go Go")
print()
pName= input("Player 1 Enter your name: ")
for i in range(1,5):
    randNo= random.randint(0,1000000)
    answer=int(input("Enter you guess: "))
    print (i)
    if answer == randNo:
        print("You guessed correct! Well done")
        exit()
    elif answer > randNo:
        print ("Too high.")
    elif answer < randNo:
        print("Too low.")
    else:
        print ("#Invalid entry, only numrical valus only.")
print ("|||Game Over|||")
print (pName," it took you,",i, " attmepts to guess the number: ",randNo)
print ("Thank you for playing")