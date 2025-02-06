import os,time
print ("30 Days of Code: Student Evaulation! ")
print ("-    -    -    -    -    -    -    -    ")
name=input("Enter your name: ")
age=input("Age in years: ")
whyCode=input ("Why learn coding?: ")
time.sleep(1)
os.system("cls")
Welcome=f"""Hey new Fellow student. Nice to meet you {name}. 
Over the years, we had so many student varying in age and background experience.
its nice to see you are just about the right age: {age} years old.
Many would say they are learning to code for $$$ reasons. No shame in that!
Its good to see you interested because {whyCode}."""
print (Welcome)
print ("-    -    -    -    -    -    -    -    ")
print ("30 Days of Code: Student Evaulation! ")
print ("-    -    -    -    -    -    -    -    ")
for i in range (1,10):
    print()
    print ("Day",i)
    answer=input("How was it? ")
    print()
    response=f"{name} your day{i} was {answer}. Great to hear that."
    print (response)
    if i==3 or i==6 or i==9 or i==12 or i==15 or i==15 or i==18 or i ==21 or i==24 or i==27:
        print  ("Ops, screen is getting cluttered. ")
        print("Lets do abit of clearing...")
        print ("-    -    -    -    -    -    -    -    ")
        print ("30 Days of Code: Student Evaulation! ")
        print ("-    -    -    -    -    -    -    -    ")
        time.sleep(2)
        os.system("cls")