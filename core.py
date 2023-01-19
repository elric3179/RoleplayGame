from random import randint
from classes import *
from math import floor
import os
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

# Fonction demandant à l'utilisateur la classe chois
# Retourne un int de 0 à 4 représentant la calsse choisi
def ask_classe(player_number):
    
    os.system("cls") # Permet de clear 
    show_classe() 
    return int(input(sayToPlayer(player_number,"choose a number:"))) - 1 

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

def interface(player_stat, actual_player, message:str):
    os.system("cls")
    print(green("╭──────────╮ "+ 15*"\t"+ " ╭──────────────────╮"))
    print(green("│ "+"Joueur "+ str(actual_player + 1)+ " │ "+ 15*"\t"+ " │ " +"Mana: "+ f"{player_stat['mana']:<2}"+ " HP: "+ f"{player_stat['hp']:<3}" + " │" ))
    print(green("╰──────────╯ "+ 15*"\t"+ " ╰──────────────────╯"))
    print(2*"\n")
    
    

    split_message = message.split("\n")
    max = 0
    for i in split_message:
        if max < len(i):
            max = len(i)

    print(5*"\t", "╭" + (max+ 3)*"─" + "╮")

    for i in range(len(split_message)):
        print(5*"\t", "│", split_message[i], (max - len(split_message[i]))*" " ,"│")

    print(5*"\t", "╰" + (max+ 3)*"─" + "╯")

# --------------------------------- Autre -----------------------------------

def game_loop(players_stats):
    actual_player = 0
    while True:
        turn(actual_player, players_stats)
        actual_player ^= 1

def turn(actual_player, players_stats):

    roll = mana_roll()
    players_stats[actual_player]["mana"] = min(players_stats[actual_player]["topMana"],players_stats[actual_player]["mana"] + roll[0])
    interface(players_stats[actual_player], actual_player, roll[1])
    input()

    



def mana_roll():
    dice_result = roll_dice(2)
    total = sum(dice_result)
    string_output = f"Lancement de dés de mana... \nVous avez obtenu {dice_result[0]} et {dice_result[1]} pour un total de {total}"
    return (total, str(string_output))
    

def play():
    players_stats = start_stat()
    print(players_stats)
    game_loop(players_stats)

play()



#interface({"class":"berseker","mana":0,"hp":100,"def":20,"topMana":40}, 0, "Hey hey")