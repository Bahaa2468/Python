print ("__Math Game___")
print ("Test Your ability to work our multiplication table")
print ("10 rounds and 10 point for every correct answer")
print()
pName= input("Player1 enter your name: ")
multipleInput= int(input("Enter the multiples: "))
round=0
score=0
point=10
for i in range(1,11):
    round+=1
    print("Round",round,": ",i," X",multipleInput)
    answer=int(input("= "))
    if answer==i*multipleInput:
        print ("Correct. 10 point")
        score+=10
    else:
        print ("Wrong, its:",i*multipleInput)

print ("||Game Over||")
print (pName,"your final score: ",score,"Points")
if score >= 80:
    print ("[Amazing Math skills. You should be proud]")
elif score >=30:
    print ("[Well done, but try better next time.]")
else:
    print ("[Nice try, you will do better next time.]")