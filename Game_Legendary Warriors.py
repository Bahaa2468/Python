print ("Welcome to Game: Legendary Warriors")
print()
print("""Information: You will be asked to name your hero/s. 
    A dice will roll twice: One with 6 sides and one with 8.
    The result will then be multiplied by 2, and your hero score reaveled.""")

def dice(sides):
    import random
    roll=random.randint(0,sides)
    return roll

for i in range (5):
    side6=dice(6)
    side8=dice(8)
    health = side6*side8*2
    character= input ("Enter character name: ")
    print ("1st dice rolled: ",side6)
    print ("1st dice rolled: ",side8)
    if health >= 30:
        print (character, "is a Legendary warrior. HP: ",health,"A mythical Warroir that long lost of this world.")
    elif health >= 25:
        print (character, "is a true warrier. HP: ",health,"A warrior that knows no rest, and all enemies are long lost.")
    elif health >= 20:
        print (character, "is a good warrier. HP: ",health,"Made of Iron and steel.")
    elif health >= 15:
        print (character, "is a warrier. HP: ",health,"Some maybe differ, but great feats are yet to be written.")
    else:
        print ("Some warriors are good for fighting, others for company. HP: ",health)