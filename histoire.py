
# By HookSander

import time     #Permet l'animation du texte en console + temps de pause + timing de l'attaque / esquive
import sys      # Permet de désactiver la mise en tampon de la console afin de permettre l'animation du texte

#!########################## CODE :

class Character :
    """Define a new Character"""
    
    def __init__(self, name, healpoint=100, weapons="Poings", damage=20, objet=None) :
        self.name = name
        self.hp = healpoint
        self.weap = weapons
        self.damage = damage
        self.objet = objet
    
    def getName(self) :
        return self.name
    
    def getHp(self) :
        return self.hp
    
    def getWeapons(self) :
        return self.weap
    
    def getDamage(self) :
        return self.damage
    
    def getObjet(self) :
        return self.objet
    
    def getNewObjet(self, nObjet) :
        animateText("\nVous venez de recevoir : {} ! \n".format(nObjet))
        self.objet = nObjet
    
    def takeDamage(self, nbr) :
        animateText("\nVous venez de subir {} de dégat...\n".format(nbr))
        self.hp -= nbr
    
    def changeWeapons(self, nName, nDamage) :
        self.weap = nName
        self.damage = nDamage
    
    def increaseHealPoint(self, nbr) :
        self.hp += nbr
        

def animateText(text):
    """Utilisable comme la commande 'print',
    mais a une animation de texte en console

    Args:
        text (Str): Le texte que l'on souhaite animer
    """
    for eachLetter in text:
        print(eachLetter, end="")
        sys.stdout.flush()  #=> Supprime la mise en tampon, afin de permettre l'animation
        time.sleep(0.02)
    
def displayInfo(info) :
    """Affiche toute les informations de l'objet info

    Args:
        info (class): L'objet dont on souhaite obtenir les informations
    """
    animateText("\nNom du joueur : {}\nPoints de vie = {}\nArme = {}\nDégats = {}\n".format(
        info.getName(), info.getHp(), info.getWeapons(), info.getDamage()
    ))

def create(name) :
    """Permet a l'utilisateur de créer un objet avec son nom 

    Args:
        name (str): Nom que le joueur souhaite utiliser duran sa partie_

    Returns:
        _class_: Renvoie un objet de la class character créer avec le bon noms
    """
    pers = Character(name)
    return pers



def attack() :
    """Interaction pour savoir si le joueur a bien appuyer sur la touche entrer
    suffisament de fois durant le temps imparti
    """
    endLoop = False
    while not endLoop :
        animateText("Appuyer 5 fois sur entrer pour attaquer, mais faite vite !!!")
        time1 = time.time()
        for i in range(5) :
            var = input("Plus que {} fois ...".format(5-(i+1)))
        time2 = time.time()
        if time2 - time1 <= 3 :
            endLoop = True
            animateText("\nBien joué !!")
        if time2 - time1 > 3 :
            animateText("\nPas assez rapide !! Essaye a nouveau...\n")

def avoid() :
    """Interaction pour savoir si le joueur a bien appuyer sur la touche entrer
    suffisament de fois durant le temps imparti
    """
    endLoop = False
    while not endLoop :
        animateText("Appuyer 5 fois sur entrer pour esquiver, mais faite vite !!!")
        time1 = time.time()
        for i in range(5) :
            var = input("Plus que {} fois ...".format(5-(i+1)))
        time2 = time.time()
        if time1 - time2 <= 3 :
            endLoop = True
            animateText("\nBien joué !!")
        else :
            animateText("\nPas assez rapide !! Essaye a nouveau...\n")


animateText("Veuillez entrer votre Nom : ") 
player = create(input(""))    # Création du personnage controlé par le joueur
monsterAfterFall = Character("Exterminator", healpoint=100, weapons="Hache", damage=100)    # Création du boss 1
bigBoss = Character("TERMINATOR", healpoint=100, weapons="Spectre du grand Magicien", damage=100, objet="Relique Magique") # Création du boss 2

#!######## Texte :
# Tout les textes nécessaire a la partie 1
#?### First Part
intro = "\nBonjour Cher {} ... \nAfin de sauver ta planète, tu vas devoir récupérer une relique magique\n\n\nMais attention, le chemin ne sera pas sans embuche".format(player.getName())
introNext = "\n\nPour vous aider je peux seulement soit te donner  : \n\n1 : Une épee qui pourra améliorer considérablement tes dégats\n...Ou alors...\n2 : Une Potion qui te donnera 100 points de vie supplémentaire."

question = "\nQuelle est ton choix ... ? [1/2]\n=> "

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


#?### Second Part :
# Tout les textes nécessaire pour la partie 2
secondIntro = "\nContent de vous revoir {}, félicitation vous y êtes presque\nJe sens qu'un grand danger vous guette...\n\nVoici une épée magique qui est la meilleur jamais forgée ...".format(player.getName())
alert = "\nAttention, quelque chose court sur vous !!!\nQuelle stratégie souhaitez vous utiliser ? : 1 = Agressif / 2 = Défensif\n"

offenChoice = "\nGrace a votre nouvelle épée, vous êtes beaucoup plus puissant ! Excellent choix !\n"
defenChoice = "\nGrace a votre expérience acquise, vous êtes beaucoup plus rapide ! Excellent choix !\n"

terminatorIntroduce = "\nAventurier ...\n\nJe suis {} et tu n'as malheureusement aucune chance contre moi ...\n".format(bigBoss.getName())

terminatorEnd = "\nNOOOOON COMMENT EST-CE POSSIBLE ?????\n\n\nBravo {} Tu as sauvé ta planète !!!".format(player.getName())


#!### GAME :


#?## First Part ==============
animateText(intro)  # Affiche les bons texte (pareil pour toute les commandes 'animeText' qui suivent)
displayInfo(player) #Affiche les infos du joueur
animateText(introNext)
animateText(question)

userChoice1 = eval(input("")) # 1 ou 2 suivant le choix du joueur
if userChoice1 == 1 :   #Parcours avec l'épée ...
    animateText(chooseSword)
    animateText("Vous venez de récupérer une Epée qui inflige 50 de dégats !")
    player.changeWeapons("Epee", 50)
    displayInfo(player) # Affiche les nouvelles infos du joueur
    
    animateText(fallCat)    
    userChoice2 = eval(input("=> "))
    if userChoice2 == 1 :   # Le joueur s'approche du de la plaque et tombe dedans
        animateText(ifFall)
        animateText(enigma) # Engime
        animateText(enigmaSuite)
        userEntry = input("\n=> ").lower()  # Réponse a l'enigme
        if userEntry == 'h' :   # si enigme juste
            animateText(notFall)
            animateText(notFallInCat)
            player.increaseHealPoint(100)
            displayInfo(player)
        if userEntry != 'h' :   # Si enigme fausse
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
    userChoice2 = eval(input(""))
    if userChoice2 == 1 :   # Si le joueur s'approche de la neige et la traverse
        animateText(ifFall)
        animateText(enigma)
        animateText(enigmaSuite)
        userEntry = input("\n=> ").lower()  # Réponse a l'énigme
        if userEntry == 'h' :   # Enigme juste
            animateText(notFall)
            animateText(notFallInMon)
            player.changeWeapons("Epée", 50)
            displayInfo(player)
        if userEntry != 'h' :   # Enigme fausse
            animateText(answer)
            player.takeDamage(monsterAfterFall.getDamage())
            animateText("Grace a votre précédent choix, vous être encore en vie, il ne vous reste plus que {} points de vie.\n\n".format(player.getHp()))


time.sleep(2)
#?#### Second Part :

animateText(secondIntro)
player.changeWeapons("Epée Magique", 100)
displayInfo(player)
animateText(alert)
userChoice1 = eval(input(" => "))
if userChoice1 == 1 :   # Choix aggresif
    animateText(offenChoice)
    animateText(terminatorIntroduce)
    attack()    # Appuyer vite sur 5 fois entrer
    time.sleep(2)
    animateText(terminatorEnd)
    player.getNewObjet(bigBoss.getObjet())

if userChoice1 == 2 :   # Choix défensif
    animateText(defenChoice)
    animateText(terminatorIntroduce)
    avoid()     # Appuyer vite sur 5 fois entrer
    time.sleep(2)
    animateText(terminatorEnd)
    player.getNewObjet(bigBoss.getObjet())
    
    

time.sleep(5)
var = input("Appuyer sur entrer pour quitter le programme")
exit()