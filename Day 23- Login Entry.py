print ("Account Login in System")
print ()

def loginPass():
    loginEntry=input("Username: ")
    passEntry= input("Password: ")
    if loginEntry=="Ali" and passEntry=="Ali1234":
        print ("Welcome",loginEntry,"Successfully logged in.")
    else:
        print ("\Incorrect Username or password")

for i in range(3):
    print (loginPass())
print ("You have exceeded logins attempts.")
print ("|| System locked: Cool down initied. ||")
