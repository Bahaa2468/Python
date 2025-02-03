print ("__Math Game___")
print ("Test Your ability to work our multiplication table")
print ("10 rounds and 10 point for every correct answer")
print()
pName= input("Player1 enter your name: ")
multipleInput= int(input("Enter the multiples: "))
round=0
score=0
point=10
for round in range(10):
    round+=1
    print("Round",round,": 1 X",multipleInput)
    question1=int(input("= "))
    if question1 == 1*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",1*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 2 X",multipleInput)
    question2=int(input("= "))
    if question2 == 2*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",2*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 3 X",multipleInput)
    question3=int(input("= "))
    if question3 == 3*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",3*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 4 X",multipleInput)
    question4=int(input("= "))
    if question4 == 4*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",4*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 5 X",multipleInput)
    question5=int(input("= "))
    if question5 == 5*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",5*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 6 X",multipleInput)
    question6=int(input("= "))
    if question6 == 6*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",6*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 7 X",multipleInput)
    question7=int(input("= "))
    if question7 == 7*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",7*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 8 X",multipleInput)
    question8=int(input("= "))
    if question8 == 8*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",8*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 9 X",multipleInput)
    question9=int(input("= "))
    if question9 == 9*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",9*multipleInput)
        print ("Score= ",score)
    print ()
    round+=1
    print("Round",round,": 10 X",multipleInput)
    question10=int(input("= "))
    if question10 == 10*multipleInput:
        print ("Well done. (10+ points)")
        score+=point
        print ("Score= ",score)
    else:
        print ("Ah, wrong. Its: ",10*multipleInput)
        print ("Score= ",score)
        print ()
    if round==10:
        break
print ("||Game Over||")
print (pName,"your final score: ",score,"Points")
if score >= 80:
    print ("[Amazing Math skills. You should be proud]")
elif score >=50:
    print ("[Well done, but try better next time.]")
else:
    print ("[Nice try, you will do better next time.]")