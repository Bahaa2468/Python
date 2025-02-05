print ("One Million to One")
print (""" In this game you get to guess the correct number.
       The game will guide you, if your guess is:
       1- Ridiculously low.
       2- A bit low
       3- A bit high
       4- Ridiculously high""")
print()
print ("Ready... Steady ... Go Go Go")
print()
pName= input ("Enter your player name: ")
number = 0
round  = 0

while number != 499999:
    round +=1
    print ("Round:",round)
    guess_Number = int(input("Enter your guess: "))
    print (pName," you entered number:",guess_Number)
    if guess_Number >= 800000:
        print ("Your guess is high. Here is a hint:")
        print ("The first digit start with: 4")
    elif guess_Number >= 500000:
        print ("Your guess is a bit high. Here is a hint:")
        print ("The third & fourth digits are also: 99")
    elif guess_Number == 499999:
        break
    elif guess_Number >= 250000:
        print ("Your guess is a bit low. Here is a hint:")
        print ("The third & fourth digits are also: 99")
    elif guess_Number >= 0:
        print ("Your guess is a Ridiculously low. Here is a hint:")
        print ("The 5th digit is like the 2nd,3rd,4th.")
    elif guess_Number < 0:
        print ("Oh Dear lord?! Did you just entered",guess_Number)
        print ("Game Over")
        print ("Good bye")
        exit()
    else:
        print ("#Invalid entry. Please enter a number!")
print ("Congratulations!,",pName)
print ("You guessed the correct number: 499999")
print ("On round:",round)
print ("Thank you for playing")
