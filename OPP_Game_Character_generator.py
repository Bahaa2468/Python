print("OOP Project Day: Game Character Generator")
import random

class character:
    name=None
    health=None
    magicpoints=None

    def healthGen():
        healthvalue=random.randint(0,1000)
        return healthvalue

    def magicGen():
        magicvalue=random.randint(0,100)
        return magicvalue
    
    def strengthGen():
        strengthvalue=random.randint(0,50)
        return strengthvalue

    def speedGen():
        speedvalue=random.randint(0,20)
        return speedvalue
    
    def __init__(self,name,health,magicpoints):
        self.name=name
        self.health=health
        self.magicpoints=magicpoints
    
    def print(self):
        print()
        print(f"This is the mighty {self.name} | with health points {self.health} and magic points: {self.magicpoints}")

class player(character):
    nickname=None
    lives=3

    def __init__(self, name, health, magicpoints,nickname):
        self.name=name
        self.health=health
        self.magicpoints=magicpoints
        self.nickname=nickname

    def print(self):
        print()
        print(f"This is the mighty {self.name} | with health points {self.health}, magic points: {self.magicpoints}. You may call him: {self.nickname}")

class enemy(character):
    type=None
    strength=None

    def __init__(self, name, type, strength):
        self.name=name
        self.type=type
        self.strength=strength

    def print(self):
        print()
        print(f"This dark nemesis:{self.name} | with type {self.type}, and strength:{self.strength}.")

class orc(enemy):
    speed=None

    def __init__(self,name,type,strength,speed):
        self.speed=speed
        self.name=name
        self.type=type
        self.strength=strength

    def print(self):
        print()
        print(f"The infamous monstrosity {self.name}, type: {self.type}, strength: {self.strength} and speed: {self.speed}")

characterInfo=character("Thor",character.healthGen(),character.magicGen())
thePlayer=player("Mighty One",character.healthGen(),character.magicGen(),"Gorg")
theEnemy=enemy("Chocolate","Class A Evil",character.strengthGen())
orcEnemy=orc("Gorbag","Guldur",character.strengthGen(),character.speedGen())
characterInfo.print()
thePlayer.print()
theEnemy.print()
orcEnemy.print()