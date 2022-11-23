
# By HookSander

from time import sleep
import sys

#!########################## CODE :

class Character :
    """Define a new Character"""
    
    def __init__(self, name, healpoint=100, weapons="Poings", damage=20) :
        self.name = name
        self.hp = healpoint
        self.weap = weapons
        self.damage = damage
    
    def getName(self) :
        return self.name
    
    def getHp(self) :
        return str(self.hp)
    
    def getWeapons(self) :
        return self.weap
    
    def getDamage(self) :
        return str(self.damage)
    
    def takeDamage(self, nbr) :
        self.hp -= nbr
    
    def changeWeapons(self, nName, nDamage) :
        self.weap = nName
        self.damage = nDamage
        

def animateText(text):
    for eachLetter in text:
        print(eachLetter, end="")
        sys.stdout.flush()  #=> Supprime la mise en tampon, afin de permettre l'animation
        sleep(0.05)
    
def displayInfo(info) :
    print("Nom du joueur : {}\nPoints de vie = {}\nArme = {}\nDégats = {}\n".format(
        info.getName(), info.getHp(), info.getWeapons(), info.getDamage()
    ))

def create(name) :
    pers = Character(name)
    return pers

#!######## Texte :
intro = "\nBonjour Cher Aventurier ... \nAfin de sauver ta planète, tu vas devoir récupérer une relique magique\n\n\nMais attention, le chemin ne sera pas sans embuche"
introNext = "\n\nPour vous aider je peux seulement soit te donner  : \n\nUne épee qui pourra améliorer considérablement tes dégats\n...Ou alors...\nUne Potion qui te donnera 100 points de vie supplémentaire."

chooseSword = "\nExcellent choix, dans les catacombes un monstre vous attend surement, rester sur vos garde !\n"

choosePotion = "\nChoix très sage, ce sera surement au sommet de la montagne qu'un adversaire vous défiera.\n"

fallCat = "* Vous tombez nez a nez avec une plaque d'aspect particulier *\nVoulez vous vous en approcher ?\n=> "
fallMon = "* Vous apercevez un monticule de neige qui attire votre attention *\nVoulez vous vous en approcher ?\n=> "