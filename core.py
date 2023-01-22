from random import randint
from classes import *
#Reading input from console (arrows)
from math import floor
from time import sleep
import os,msvcrt,sys

# ------------------------- Mapping des couleurs --------------------------
red         = lambda string: "\033[1;31m" + string + "\033[0;00m"
green       = lambda string: "\033[1;32m" + string + "\033[0;00m"
darkgreen       = lambda string: "\033[0;32m" + string + "\033[0;00m"
# ----------------------- Mapping des pourcentages ------------------------

# Permet de déterminer un pourcentage d'éfficacité de l'attaque en fonction d'un résulat d'un dé
diceMappings = {
    1 : 0.65,
    2 : 0.8,
    3 : 1,
    4 : 1,
    5 : 1.1,
    6 : 1.25
}

#Permet de déterminer l'éfficacité en fonction de la défense
defenseCalculator = lambda attack, defense : attack / (1+(defense/100))

# -------------------------- Gestion des stats ----------------------------

attackerStatsList = ["mana","hp","def"]
defenderStatsList = ["atthp","attmana"]

# --------------------------- Lancement de dés -----------------------------

# Permet de lancer un nombre donné de dés
# Retourne une liste contenant les résultats des lancer
def roll_dice(dice_number) -> list:
    result = []
    for i in range(dice_number):
        result.append(dice())
    return result


# Fonction de lancemment de dés
# Retourne entre 1 et 6
def dice():
    return randint(1, 6)

# Calculer le valeur associé a une compétence une fois un dé lancer
def amountDiced(diceNum:int,attackAmount:int) -> int:
    return floor(attackAmount * diceMappings[diceNum])

# --------------------------- Gestion des classes ---------------------------

# Fonction demandant à l'utilisateur la classe choisie
# Retourne un int de 0 à 4 représentant la classe choisie
def ask_classe(player_number):
    classIndex = 0
    while True:
        os.system("cls") # Permet de clear 
        show_classe(classIndex)
        sys.stdout.flush()
        char = msvcrt.getch()
        match char:
            case b"P":
                classIndex = min(3,classIndex+1)
            case b"H":
                classIndex = max(0,classIndex-1)
            case b"\n" | b"\r" | b"\r\n" | b"\n\r":
                break
    return int(classIndex)

# Gère la sélection de classe pour les 2 joueurs
# Retourne une liste de deux nombre dans l'intervalle [0; 3] représentant la classe choisi
def classes_selection():
    choose_class = []
    for i in range(2):
        choose_class.append(ask_classe(i + 1))
    return choose_class

# Lancement du système de stat et donc du système de classe
# Retourne une liste des stats de chaque joueur
def start_stat() -> list:
    choosen_class = classes_selection()
    players_stats_start = []
    for i in range(len(choosen_class)):
        players_stats_start.append(stats(get_classes(choosen_class[i])))
    return players_stats_start

# ----------------------------- Competence ----------------------------------

# Fonction appellé a l'utilisation d'une compétence demande les statistiques des 2 joueurs et les modifie en fonction de la compétence et d'un lancer de dé
# Retourne les statistique des 2 joueurs
def attackRoll(attack:tuple[str,int,dict,str], attackerStats:dict, defenderStats:dict):
    roll = dice()
    for i in attack[2].keys():
        if i in defenderStatsList:
            defenderStats[i[3:]] = max(0,defenseCalculator(defenderStats[i[3:]]-amountDiced(roll, attack[2][i]),defenderStats["def"]))
        elif i in attackerStatsList:
            if i == "mana":
                attackerStats[i] = min(attackerStats["topMana"],attackerStats[i] + amountDiced(roll,attack[2][i]))
            else:
                attackerStats[i] += amountDiced(roll, attack[2][i])

    return [attackerStats, defenderStats]


# ----------------------------- Utilitaire ----------------------------------

# Créer un string placé sur la bordure droite de la fênetre de commande en fonction d'un texte
# Retourne un texte situé sur la limite droite de la fênetre
def border(text:str) -> str:
    return (os.get_terminal_size().columns - len(text)) * " " + text

# Crée un string placé sur le centre de la fênetre de commande en fonction d'un texte
# Retourne un texte situé sur le centre de la fênetre
def center(string: str) -> str:
    return int(((os.get_terminal_size().columns / 2) - (len(string) / 2)))*" " + string

# Crée des chaines de caractère pour l'affichage d'un joueur en fonction de ces statistiques
# Retourne une liste de string pret a l'emploi
def player_menu(player_stat, player_number):
    text_result = []

    text_result.append("╭" +20*"─" + "╮")
    text_result.append(("│ " + "Joueur " + str(player_number + 1) + 11*" " +  "│" ))
    text_result.append(("│ " + "Classe: " + f"{player_stat['class']:<11}" + "│"))
    text_result.append(("│ " +"Mana: "+ f"{player_stat['mana']:<2}"+ " HP: "+ f"{player_stat['hp']:<3}"  + 3*" "+ "│"))
    text_result.append("╰" +20*"─" + "╯")
    return text_result


def chooseFirstPlayer(players_stat: list) -> list:
    for i in range(9):
        os.system("cls")
        dots = "."*(i%3+1)
        displayCustomMessage(f"Choosing random number{dots:<3}")
        sleep(0.3)
    choosen = randint(0,1)
    if choosen == 1:
        players_stat.reverse()
        
    return [choosen, players_stat]

def sayWhoIsFirst(number:int):
    os.system("cls")
    displayCustomMessage(f"Le premier joueur est le numéro {number}")

# Permet l'affichage d'un message custom dans le format de l'affichage
# Ne retourne rien
def displayCustomMessage(message):
    #Display the custom message
    split_message = message.split("\n")
    max_len = len(max(split_message, key=len))
    
    print(center(("╭" + (max_len)*"─" + "╮")))

    for i in range(len(split_message)):
        text = "".join(("│", split_message[i], (max_len - len(split_message[i]))*" " ,"│"))
        print(center(text))

    print(center("╰" + (max_len)*"─" + "╯"))

# Gére l'affichage d'une interface montrant toute les informations principales au joueurs
# Ne retourne rien
def interface(players_stat, actual_player, message:str):
    os.system("cls")

    other_player = actual_player ^1
    for i in player_menu(players_stat[1], other_player):
        print(red(border(i)))

    print(5*"\n")

    for i in player_menu(players_stat[0], actual_player):
        print(green(i))

    print(2*"\n")
    displayCustomMessage(message)
# --------------------------------- Autre -----------------------------------


# Fonction gérant la boucle de jeu et le changement de joueur pour chaque tour
def game_loop(players_stats:list):
    choosen = chooseFirstPlayer(players_stats)
    actual_player  = choosen[0]
    players_stats = choosen[1]
    sayWhoIsFirst(actual_player+1)
    sleep(1)
    while True:
        players_stats = turn(actual_player, players_stats)
        actual_player ^= 1
        players_stats.reverse()

def turn(actual_player, players_stats):

    roll = mana_roll()
    players_stats[0]["mana"] = min(players_stats[0]["topMana"],players_stats[0]["mana"] + roll[0])
    interface(players_stats, actual_player, roll[1])
    print()
    input(players_stats)
    competence = None
    while competence == None:

        interface(players_stats, actual_player, display_competence(players_stats[0]["class"]))
        competence = select_competences(players_stats[0]["class"])   
        if competence == None:
            h= 0
        elif competence == 5:
            # Pour ne pas rentrer dans une erreur avec une cinquième compétence, qui n'existe pas
            return players_stats
        elif competence[1] > players_stats[0]["mana"]:
            interface(players_stats,actual_player,"You do not have enough mana!")
            competence = None
            sleep(2)
        else:
            players_stats[0]["mana"] -= competence[1]
            return attackRoll(competence, players_stats[0], players_stats[1])
            


def select_competences(playerclass):
    numberChoosen = input("Choisisez une compétence (numéro): ")
    if numberChoosen not in ["1","2","3","4","5"]:
        return None
    
    else:
        numberChoosen = int(numberChoosen) - 1
    
    if numberChoosen == 4:
        return 5

    return competences(playerclass)[numberChoosen]

def display_competence(player_class):
    comp = competences(player_class)
    display_text = "Competences:"
    for i in range(len(comp)):
        display_text += f"\n{i + 1}: {comp[i][0]}, {comp[i][3]} ;  {comp[i][1]} mana"
    display_text += f"\n5: Keep the mana"
    return display_text



def mana_roll():
    dice_result = roll_dice(2)
    total = sum(dice_result)
    string_output = f"Lancement de dés de mana... \nVous avez obtenu {dice_result[0]} et {dice_result[1]} pour un total de {total}"
    return (total, (string_output))
    

def play():
    players_stats = start_stat()
    game_loop(players_stats)

play()
