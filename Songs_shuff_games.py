import random,os,time
print("Songs Game")
def randGen():
    num=random.randint(0,19)
    return num
games=0
song1="Hit me Baby One more Time"
artist1="Britney Spears"
song1_list=["Hit","Me","Baby","One","More","Time"]
song1_shufful=random.choices(song1_list,weights=[3,3,3,2,2,1],k=20)
songs1_updated=song1_shufful

while True:
    games+=1
    print(f"You have {games} to win")
    choice=print(songs1_updated[randGen()])
    player1=input("Text here: ")
    #here the rule should be if the choice in the list to remove and updated the list
    #pseudo code:
    #1- The player entry is compared to a list. 
    #2- If the entry is found in the list, the list entry is removed.
    #3- should all  entries are inserted correctly, and before the games counter reaches 20.
    #4- player wins.
    if games==20:
        print("== Game Over ==")
        print("The song is: ")
        print(f"Title: {song1}")
        print(f"By: {artist1}")
        otherchoice=input("Again? Press Enter. Quit the program press (e): ")
        if otherchoice =="e":
            break
        else:
            continue
