from random import randint
from classes import *
import os

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

# -------------------------------- Autres ----------------------------------

def sayToPlayer(num,text) -> str:
    return f"Player {num}, {text} "


def game_loop(players_stats):
    actual_player = 0
    while True:
        os.system("cls")
        print(sayToPlayer(actual_player + 1, "it's your turn"))
        players_stats[0]["mana"] += mana_roll()
        actual_player ^= 1


def mana_roll():
    
    print("Lancement de dés de mana...")
    dice_result = roll_dice(2)
    total = sum(dice_result)
    print("Vous avez obtenu", dice_result[0], "et", dice_result[1], "pour un total de", total)
    return total
    



def play():
    players_stats = start_stat()
    print(players_stats)
    game_loop(players_stats)

play()
