
#! By HookSander

class Weapons :
    """All weapons"""

    def __init__ (self, name, damage) :
        self.name = name
        self.damage = damage
    


class Character :
    """Define a character"""

    def __init__ (self, name, weapons, lifePoint=100, damage=5) :
        
        self.name = name
        self.lifePoint = lifePoint
        self.weapons = weapons
        self.damage = damage

    def attack(self, otherCharacter) :
        otherCharacter.lifePoint -= self.damage
    
    def changeName(self, newName) :
        self.name = newName
    
    def attacked(self, otherCharacter) :
        self.lifePoint -= otherCharacter.damage
    
    def getLifePoint(self) :
        return "{} a {} pv restant.".format(self.name, self.lifePoint)
    
    def getDamage(self) :
        return "L'attaque de {} enlève {} point de vie".format(self.name, self.damage)
    
    def getName(self) :
        return self.name
    
    def getCurrentWeapons(self) :
        return "L'arme équipée est : {}".format(self.weapons)