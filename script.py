
#! By HookSander

class Character :
    """Define a character"""

    def __init__ (self, name="Default", lifePoint=100, weapons="pistol", damage=10) :
        
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