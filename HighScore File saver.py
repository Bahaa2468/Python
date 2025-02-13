print ("HighScore saved files")
f=open("HighScore.txt","a+")
exit=""
while exit !="e":
    letters=input("Enter 3 Letters: ")
    score=int(input("Score: "))
    if score >= 100001:
        print("Max Score allowed 100000")
    exit=input("Add another one(a), or exit (e):")
    if exit =="e":
        break
print()
print("Added")
f.write(f"{letters:>3}:  {score:>3}\n")
f.close()

