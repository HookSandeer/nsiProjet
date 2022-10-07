
#! By HookSandeer

import random


class Charactere :
    """Create charactere class"""

    def __init__(self, name, healpoint=100, damage=20):
        self.name = name
        self.healpoint = healpoint
        self.damage = damage

    def getName(self) :
        return self.name
    
    def getHealpoint(self) :
        return self.healpoint
    
    def getDamage(self) :
        return self.damage
    
    def attack(self, otherCharacter) :
        print("{} attaqe {}, ce qui lui inflige {}".format(self.name, otherCharacter.name, self.damage))
        otherCharacter.healpoint -= self.healpoint
    

def createPlayer() :
    userName = input("\nEntrer le nom du joueur 1 \n=>")
    player = Charactere(userName)
    return player

def randomNum():
    return random.randint(1, 10)

def random1Or2() :
    return random.randint(1, 2)

def begin() :
    if random1Or2() == 1 :
        print("{} commence !".format(j1.getName()))
        a = randomNum(), b=randomNum()
        listeCalc = [a, b, a*b]
        res = eval(input("Combien font {} x {}".format(listeCalc[0], listeCalc[1])))
        if res == listeCalc[2] :
            return True
        else :
            return False


j1 = createPlayer()
j2 = createPlayer()

count = 0
while j1.getHealpoint() != 0 or j2.getHealpoint() !=0 :
    count += 1