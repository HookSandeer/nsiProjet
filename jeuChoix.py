
# By HookSander

import time

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


# Lancement du jeux :

def effetTexte(texte) :
    for i in range(len(texte)) :
        print(texte[i],  end="")
        time.sleep(0.03)

effetTexte("Bonjour cher aventurier !\n\n")
effetTexte("Bienvenu dans cette aventure !\n\n")
effetTexte("Pour sauver ta planète tu vas devoir trouver une relique, mais attention, \n\n\n\n")
time.sleep(0.3)
effetTexte("Le chemin ne sera en aucun cas facile, et tu devras affronter des adversaires très puissant\n")