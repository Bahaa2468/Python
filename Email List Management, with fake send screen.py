import os,time
print ("-    -    -    -    -    ")
print ("Email list Management")
print ("-    -    -    -    -    ")
time.sleep(3)
os.system("cls")
emailList=[]

def emaillistPrinting():
    os.system("cls")
    for index in range(len(emailList)):
        print(f"{index}.{emailList[index]}")


while True:
    action=input ("1.Add email\n2.Remove Email\n3.View Email\n4.Send Emails.\n")
    if action=="1":
        email=input ("Email:")
        emailList.append(email)
        time.sleep(1)
        os.system("cls")
    elif action =="2":
        email=input("Remove: ")
        if email in emailList:
            emailList.remove(email)
            print(f"{email} removed!")
        else:
            print(f"{email} is not on the list!")
        time.sleep(1)
        os.system("cls")

    elif action =="3":
        while True:
            os.system("cls")
            emaillistPrinting()
            end=input("To return to main menu, press any key:")
            if end == "NoStay":
                print ("Congrats. You discovered my first Easter Egg! Tell your friends")
            else:
                os.system("cls")
                break
        time.sleep(5)
    elif action =="4":
        os.system("cls")
        for i in range(0,10000):
            print("Email:",i,"sending")
            time.sleep(0.1)
            print("Email:",i,"sent.")
            time.sleep(0.2)
            os.system("cls")

    else:
        print ("Invalid Entry ... please enter 1/2/3 or 4")
        continue