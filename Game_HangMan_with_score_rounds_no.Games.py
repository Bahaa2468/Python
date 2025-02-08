import random,os,time
score=0
game=0
while True:
    print ("-    -    -    -    ")
    print ("Game: Hang man")
    print ("-    -    -    -    ")   
    print ("You have 10 rounds to guess the letters inside a word.")
    print ("+10 points for right guess.")
    print ("-    -    -    -    ")   
    print("Your game score: ",score)
    print(f"You played {game} games")
    time.sleep(5)
    os.system("cls")
    wordlist=["easy","beauty","sample","machine","crab","dance","apple","animal","advice","ciname"]
    wordRand=random.choice(wordlist)
    letter=[]
    round=0

    while round<10:
        time.sleep(1)
        os.system("cls")
        round+=1
        print (f"Round: {round}")
        for i in wordRand:
            if i in letter:
                print (f"{i}",end=" ")
            else:
                print("_",end=" ")
        print ()
        userchoice=input("choose a letter: ").strip().lower()
        print ()
        if userchoice in letter:
            print ("Letter already choosen.")
        elif userchoice in wordRand:
            print("Congratulation. You have successfully guessed the right letter")
            letter.append(userchoice)
            score+=10
        else:
            print ("Letter is not the word. Try a different one.")
        if all(i in letter for i in wordRand):
            print (f"Congratulations. You won! You guessed the word: {wordRand}, your score: {score}")
            game+=1
            break
    print("Game Over")
    game+=1
    again=input(f"Press enter to play again, or (e) to exit:\n").strip().lower
    if again=="e":
        print(f"You played {game} games")
        print (f"Thank you for playing. Your final score:{score} Come back and get a better one")
        break
    else:
        continue

