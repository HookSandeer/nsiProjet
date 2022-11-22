
# By HookSander 

import random

class Weapon :
    """Define new weapons"""

    def __init__(self, name, magazine, damage) :
        self.name = name
        self.mag = magazine
        self.damage = damage
    
    def getName(self) :
        return self.name
    
    def getMag(self) :
        return self.mag
    
    def getDamage(self) :
        return self.damage
    



class Character :
    """Define a new charactere"""

    def __init__(self, name, weapon, healPoints=100) :
        self.name = name
        self.weapon = weapon
        self.hp = healPoints
    
    def getName(self) :
        return self.name
    
    def getWeapons(self) :
        return self.weapon.getName
    
    def getHp(self) :
        return self.hp
    
    def takeDamage(self, nbr) :
        self.hp -= nbr
    
    def attack(self, otherPlayer) :
        otherPlayer.takeDamage(self.hp)
        print("{} a infligé {} dégats a {}. Il lui reste {} points de vie".format(
            self.name, self.weapon.getDamage(), otherPlayer.getHp()
        ))


def randomWeapon() :
    liste = []
    AssaultRifle = Weapon("Ak-47", "30", "25")
    liste.append(AssaultRifle)
    



def createPlayer(UserName)