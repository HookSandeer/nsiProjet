
#! By HookSandeer

import random

botListName = [
    "TheKiller", "The Punisher", "Preadator", "Alien", "James Bond", "Rocky", "Terminator"
]

weaponsList = {
    "Pistolet" : "13",
    "Fusil d'assault" : "36",
    "Fusil à pompe" : "42",
    "Fusil de sniper" : "62"
}

randomList = random.shuffle(["Pistolet", "Fusil d'assault", "Fusil à pompe", "Fusil de sniper"])

class Character :
    """Define a new character"""
    
    def __init__(self, name, lifepoint, listIndex) :
        self.name = name
        self.lifepoint = lifepoint
        self.weapons = randomList[listIndex]
        self.damage = weaponsList(randomList[listIndex])
        
    
    def attack(self, otherPlayer) :
        print("Le joueur {} possèdant {} a subit une attaque de {} lui inffligeant {} dégat").format(
            self.name, self.lifepoint, otherPlayer.name, otherPlayer.damage
        )
        self.lifepoint -= otherPlayer.damage
        if self.lifepoint >= 0 :
            pass
    
    def getattributeName(self) :
        return self.name
    
    def getattributeLifePoint(self) :
        return self.lifepoint
    
    def getattributeDamage(self) :
        return self.damage
    
    def getattributeWeapons(self) :
        return self.weapons
    
def botPlayer1(nameList) :
    botPlayerName = nameList[random.randint(0, len(nameList)-1)]
    bot1 = Character(botPlayerName, 100, random.randint(0, 3))
    print("Le bot 1 a été généré correctement.")
    return bot1

def botPlayer2(nameList) :
    botPlayerName = nameList[random.randint(0, len(nameList)-1)]
    bot2 = Character(botPlayerName, 100, random.randint(0, 3))
    print("Le bot 2 a été généré correctement")
    return bot2

def player1() :
    userName = input("Entrer le pseudo du joueur 1 \n=> ")
    player1 = Character(userName, 100, random.randint(0, 3))
    print("Le joueur {} a bien été validé !").format(userName)
    return player1

def player2() :
    userName = input("Entrer le pseudo du joueur 2\n=> ")
    player2 = Character(userName, 100, random.randint(0, 3))
    print("Le joueur {} a bien été validé !").format(userName)
    return player2

