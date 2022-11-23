
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
        return self.hp
    
    def getWeapons(self) :
        return self.weap
    
    def getDamage(self) :
        return self.damage
    
    def takeDamage(self, nbr) :
        animateText("\nVous venez de subir {}".format(nbr))
        self.hp -= nbr
    
    def changeWeapons(self, nName, nDamage) :
        self.weap = nName
        self.damage = nDamage
    
    def increaseHealPoint(self, nbr) :
        self.hp += nbr
        

def animateText(text):
    for eachLetter in text:
        print(eachLetter, end="")
        sys.stdout.flush()  #=> Supprime la mise en tampon, afin de permettre l'animation
        sleep(0)
    
def displayInfo(info) :
    animateText("\nNom du joueur : {}\nPoints de vie = {}\nArme = {}\nDégats = {}\n".format(
        info.getName(), info.getHp(), info.getWeapons(), info.getDamage()
    ))

def create(name) :
    pers = Character(name)
    return pers

animateText("Veuillez entrer votre Nom : ")
player = create(input())
monsterAfterFall = Character("Exterminator", healpoint=100, weapons="Hache", damage=100)

#!######## Texte :
intro = "\nBonjour Cher {} ... \nAfin de sauver ta planète, tu vas devoir récupérer une relique magique\n\n\nMais attention, le chemin ne sera pas sans embuche".format(player.getName())
introNext = "\n\nPour vous aider je peux seulement soit te donner  : \n\n1 : Une épee qui pourra améliorer considérablement tes dégats\n...Ou alors...\n2 : Une Potion qui te donnera 100 points de vie supplémentaire."

question = "\nQuelle est ton choix ... ? [1/2]"

chooseSword = "\nExcellent choix, dans les catacombes un monstre vous attend surement, rester sur vos garde !\n"

choosePotion = "\nChoix très sage, ce sera surement au sommet de la montagne qu'un adversaire vous défiera.\n"

fallCat = "\n* Vous tombez nez a nez avec une plaque d'aspect particulier *\nVoulez vous vous en approcher ? 1 = Oui / 2 = Non\n=> "
fallMon = "\n* Vous apercevez un monticule de neige qui attire votre attention *\nVoulez vous vous en approcher ? 1 = Oui / 2 = Non\n=> "

ifFall = "\n\n* KRAAAAAAAAAKKK * Vous venez de tomber dans un trou, et ... OH NON !\n Un monstre se dresse devant vous, vous barrant le chemin..."

enigma = "\nAHAHAHAHA, Salutation aventurier, j'attendais ta visite...\nJe suis le grand {}\nJe te laisse la vie sauve si tu réponds correctement à cette énigme...\n\n".format(monsterAfterFall.getName())
enigmaSuite = "Quelle est, la lettre la plus, dirons nous, TRANCHANTE ? \nChoix Possible : P / R / S / H / T"
answer = "\nMalheureusement pour toi, la réponse est H, (la Hache), tu vas DONC MOURIR"

notFall = "\nHMMMM, Bravo, mais faite attention la prochaine fois je ne serai pas aussi clément...\n"
notFallInCat = "\nFélicitation, vous venez de découvrir une potion qui vous donne 200 points de vie !\n"
notFallInMon = "\nFélicitation, vous venez de découvrir une épée qui améliore vos dégats !\n"

mountainMonster = "\nATTENTION !! \nLe monstrueu yéti des montagnes se dresse devant vous\nQuelle stratégie choisissez vous ? : 1=Agressif / 2=Défensif\n"
catacombeMonster = "\nACHTUNG !!\nLe maléfique prince des catacombes veut votre mort...\nQuelle stratégie choisissez vous ? : 1=Agressif / 2=Défensif\n"

#!### GAME :

animateText(intro)
displayInfo(player) #Affiche les infos du joueur
animateText(introNext)
animateText(question)

userChoice1 = eval(input("\n=> ")) # 1 ou 2 suivant le choix du joueur
if userChoice1 == 1 :   #Parcours avec l'épée ...
    animateText(chooseSword)
    animateText("Vous venez de récupérer une Epée qui inflige 50 de dégats !")
    player.changeWeapons("Epee", 50)
    displayInfo(player) # Affiche les nouvelles infos du joueur
    
    animateText(fallCat)
    userChoice2 = eval(input("=> "))
    if userChoice2 == 1 :
        animateText(ifFall)
        animateText(enigma)
        animateText(enigmaSuite)
        userEntry = input("\n=> ").lower()
        if userEntry == 'h' :
            animateText(notFall)
            animateText(notFallInCat)
            player.increaseHealPoint(100)
            displayInfo(player)
        if userEntry != 'h' :
            animateText(answer)
            player.takeDamage(monsterAfterFall.getDamage())
            if player.getHp() <= 0 :
                animateText("\nVous avez échoué, dommage ...")
                var = input("\n\nAppuyer sur entrer pour quitter")
                exit()
        
         

if userChoice1 == 2 :   # Parcours avec le potion de soir
    animateText(choosePotion)
    animateText("Vous venez de recevoir 100 points de vie supplémentaire ")
    player.increaseHealPoint(100)
    displayInfo(player) # Affiche les nouvelles infos du joueur
    
    animateText(fallMon)
    userChoice2 = eval(input("=> "))
    if userChoice2 == 1 :
        animateText(ifFall)
        animateText(enigma)
        animateText(enigmaSuite)
        userEntry = input("\n=> ").lower()
        if userEntry == 'h' :
            animateText(notFall)
            animateText(notFallInMon)
            player.changeWeapons("Epée", 50)
            displayInfo(player)
        if userEntry != 'h' :
            animateText(answer)
            player.takeDamage(monsterAfterFall.getDamage())
            animateText("Grace a votre précédent choix, vous être encore en vie, il ne vous reste plus que {} points de vie.".format(player.getHp()))
            

print("Tout vas bien sa mere je suis content")

var = input()