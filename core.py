from random import randint
from classes import *
#Reading input from console (arrows)
import msvcrt
from math import floor
from time import sleep
import os,msvcrt,sys

# ------------------------- Mapping des couleurs --------------------------
red         = lambda string: "\033[1;31m" + string + "\033[0;00m"
green       = lambda string: "\033[1;32m" + string + "\033[0;00m"
darkgreen       = lambda string: "\033[0;32m" + string + "\033[0;00m"
# ----------------------- Mapping des pourcentages ------------------------

diceMappings = {
    1 : 0.65,
    2 : 0.8,
    3 : 1,
    4 : 1,
    5 : 1.1,
    6 : 1.25
}

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

def classes_selection():
    choose_class = []
    for i in range(2):
        choose_class.append(ask_classe(i + 1))
    return choose_class

def start_stat() -> list:
    choosen_class = classes_selection()
    players_stats_start = []
    for i in range(len(choosen_class)):
        players_stats_start.append(stats(get_classes(choosen_class[i])))
    return players_stats_start

# ----------------------------- Competence ----------------------------------

def attackRoll(attack:tuple[str,int,dict,str], attackerStats:dict, defenderStats:dict):
    roll = dice()
    for i in attack[2].keys():
        if i in defenderStatsList:
            defenderStats[i[3:]] = max(0,defenderStats[i[3:]]-amountDiced(roll, attack[2][i]))
        elif i in attackerStatsList:
            if i == "mana":
                attackerStats[i] = min(attackerStats["topMana"],attackerStats[i] + amountDiced(roll,attack[2][i]))
            else:
                attackerStats[i] += amountDiced(roll, attack[2][i])

    return attackerStats, defenderStats

# ----------------------------- Utilitaire ----------------------------------

# Permet de creer un message (texte en argument) a destination d'un joueur donner en argument
# Retourne un string construit
def sayToPlayer(num,text) -> str:
    return f"Player {num}, {text} "

def spaceBetween(other_string, size=os.get_terminal_size().columns) -> str:
    return int(((size  - other_string)/8))*"\t"

def center(string, size=os.get_terminal_size().columns) -> str:
    return int(((size / 2) - (len(string) / 2))/8)*"\t" + string

def chooseFirstPlayer() -> int:
    for i in range(9):
        os.system("cls")
        print(red(center("╭───────────────────────────╮")))
        dots = "."*(i%3+1)
        print(red(center(f"│ Choosing random number{dots:<3} │")))
        print(red(center("╰───────────────────────────╯ ")))
        sleep(0.3)
    return randint(0,1)

def sayWhoIsFirst(number:int):
    os.system("cls")
    print(center("╭───────────────────────────────────╮"))
    print(center(f"│ Le premier joueur est le numéro {number} │"))
    print(center("╰───────────────────────────────────╯"))

def interface(player_stat, actual_player, message:str):
    os.system("cls")
    
    print(red("╭──────────╮ "+ spaceBetween(34) + " ╭──────────────────╮"))
    print(red("│ "+"Joueur "+ str(actual_player + 1)+ " │ "+ spaceBetween(34)+ " │ " +"Mana: "+ f"{player_stat['mana']:<2}"+ " HP: "+ f"{player_stat['hp']:<3}" + " │" ))
    print(red("╰──────────╯ "+ spaceBetween(34) + " ╰──────────────────╯"))
    print(2*"\n")

    split_message = message.split("\n")
    max_len = len(max(split_message, key=len))
    
    
    print(center(("╭" + (max_len)*"─" + "╮")))

    for i in range(len(split_message)):
        
        text = "".join(("│", split_message[i], (max_len - len(split_message[i]))*" " ,"│"))
        print(center(text))

    
    print(center("╰" + (max_len)*"─" + "╯"))

# --------------------------------- Autre -----------------------------------


# Fonction gérant la boucle de jeu et le changement de joueur pour chaque tour
def game_loop(players_stats:list):
    actual_player = chooseFirstPlayer()
    sayWhoIsFirst(actual_player+1)
    sleep(1)
    while True:
        turn(actual_player, players_stats)
        actual_player ^= 1
        players_stats.reverse()

def turn(actual_player, players_stats):

    roll = mana_roll()
    players_stats[0]["mana"] = min(players_stats[0]["topMana"],players_stats[0]["mana"] + roll[0])
    interface(players_stats[0], actual_player, roll[1])
    input()
    competence = None
    while competence == None:

        interface(players_stats[0], actual_player, display_competence(players_stats[0]["class"]))
        competence = select_competences(players_stats[0]["class"])   
        if competence == 5:
            # Pour ne pas rentrer dans une erreur avec une cinquième compétence, qui n'existe pas
            pass
        elif competence[1] > players_stats[0]["mana"]:
            interface(players_stats[0],actual_player,"You do not have enough mana!")
            input()
        else:
            players_stats[0]["mana"] -= competence[1]
            print(attackRoll(competence, players_stats[0], players_stats[1]))
            input()


def select_competences(playerclass):
    numberChoosen = input("Choisisez une compétence (numéro): ")
    if numberChoosen not in ["1","2","3","4","5"]:
        numberChoosen = None
    else:
        numberChoosen = int(numberChoosen) - 1
        
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
    return (total, str(string_output))
    

def play():
    players_stats = start_stat()
    game_loop(players_stats)

play()
