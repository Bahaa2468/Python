import random,os,time

def dice(sides):
    roll=random.randint(0,sides)
    return roll

def health():
    healthScore=((dice(6)*dice(12))/2)+10
    return healthScore

def strength():
    strengthScore=((dice(8)*dice(8))/2)+12
    return strengthScore

print ("__|__Epic Character Battle__|__")
print("-   -   -   -   -  ")
p1Name=input ("Player 1 enter your name: ")
p2Name=input ("Player 2 enter your name: ")
print("-   -   -   -   -  ")

while True:
    p1Hero=input ("PLayer 1 Name your Champion: ")
    p1Type=input ("Player 1 Type(Human, Troll, Elf, Wizard, Orc or Dwarf: ")
    p2Hero=input ("Player 2 Name your Champion: ")
    p2Type=input ("Player 2 Type(Human, Troll, Elf, Wizard, Orc or Dwarf: ")
    print()
    print (p1Name, "your champion: ",p1Hero)
    print ("Type: ",p1Type)
    p1Health=health()
    p1Strength=strength()
    print ("Health: ",p1Health)
    print ("Strength: ",p1Strength)
    print("-   -   -   -   -  ")
    print (p2Name, "your champion: ",p2Hero)
    print ("Type: ",p2Type)
    p2Health=health()
    p2Strength=strength()
    print ("Health: ",p2Health)
    print ("Strength: ",p2Strength)
    print ()
    print("Let the Battle Begins ...")
    time.sleep(8)
    os.system("cls")
    print (p1Hero,"is looking at",p2Name)
    print ("- Who are you? Ask",p1Hero)
    print ("- I'm ",p2Hero)
    print ("The heros clash and hit one another.")
    print ("The battle begins...............")
    time.sleep(4)
    os.system("cls")
    if p1Strength>=p2Strength:
        damage=p1Strength-p2Strength
        damage+=1
    else:
        damage=p2Strength-p1Strength
        damage+=1
    injury1=int(p1Health/damage)
    injury2=int(p2Health/damage)
    if injury1==injury2:
        print ("Draw.")
        print (p1Hero," and ",p2Hero," annihilated one another")
        print ("A moment of silence....")
        print ("Round ",injury1)
    elif injury1 > injury2:
        print ("Victory...")
        print (p1Hero," Destroyed the inforier ",p2Hero)
        print ("on Round: ",injury2)
    elif injury2 > injury1:
        print ("Victory...")
        print (p2Hero," Destroyed the inforier ",p1Hero)
        print ("on Round: ",injury1)
    print("-   -   -   -   -  ")
    print ("Player 1 name:",p1Name,", Hero:",p1Hero,", Health:",p1Health,", Strength:",p1Health)
    print ("Player 1 name:",p2Name,", Hero:",p2Hero,", Health:",p2Health,", Strength:",p2Health)
    print("-   -   -   -   -  ")
    again =input ("Again or exit: ")
    if again=="exit" or again=="Exit":
        break
    time.sleep(1)
    os.system("cls")

print ("Thank you for playing!")