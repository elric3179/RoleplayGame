from random import randint
from classes import *


# Permet de lancer un nombre donné de dés
# Retourne une liste contenant les résultats des lancer
def roll_dice(dice_number):
    result = []
    for i in range(dice_number):
        result.append(dice())
    return result


# Fonction de lancemment de dés
# Retourne entre 1 et 6
def dice():
    return randint(1, 6)

def ask_classe(player_number):
    classes = get_classes()
    for i in range(len(classes)):
        print(str(i + 1) + ": " + str(classes[i]))
    return int(input("Player " + str(player_number) + ", choose a number: ")) - 1

def classes_selection():
    choose_class = []
    for i in range(2):
        choose_class.append(ask_classe(i + 1))
    return choose_class

def start_stat():
    choosen_class = classes_selection()
    print(choosen_class)
    players_stats = []
    for i in range(len(choosen_class)):
        players_stats.append(stats(get_classes(choosen_class[i])))
    print(players_stats)

def play():
    start_stat()

play()
