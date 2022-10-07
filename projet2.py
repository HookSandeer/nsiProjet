
#! By HookSander

import random
import time

listeBotName = ["Predator", "Alien", "Terminator", "Robobot", "Rocky"]
class Weapons :
    """Define all the weapons"""

    def __init__(self, name="Poings", damage=5):
        self.name = name
        self.damage = damage
    
    def getName(self) :
        return self.name
    
    def getDamage(self) :
        return self.damage

        

class Character :
    """Define a character"""

    def __init__(self, name, weapons, level=1, healpoint=100):
        self.name = name
        self.weapons = weapons
        self.level = level
        self.healpoint = healpoint
        self.damage = damage

    def getName(self) :
        return self.getName
    
    def getWeapons(self) :
        return self.weapons.getName()
    
    def getLevel(self) :
        return self.level
    
    def getHealpoint(self) :
        return self.healpoint
    
    def getDamage(self) :
        return self.weapons.getDamage()
    
    def improveLevel(self, nbr) :
        self.level += nbr
    
    def attacked(self, damage) :
        self.healpoint -= damage
    
    def attack(self, otherPlayer) :
        return "{} a attaqué {}, ce qui lui inflige {} dégat. {} se retrouve avec {} hp.".format(
            self.name, otherPlayer.getName(), self.weapons.getDamage(), otherPlayer.getHealpoint()
        )
        otherPlayer.attacked(self.weapons.getDamage())


def createPlayer() :
    userName = input("Entrer le nom du joueur {}\n=> ")
    player = Character(userName, Weapons())
    return player

def bot1(liste) :
    bot1 = Character(liste[random.randint(0, len(liste)-1)], Weapons("Fusil", 15))
    return bot1



def random1or2() :
    return random.randint(1, 2)

def randomNum() :
    return random.randint(1, 10)