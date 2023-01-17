from random import randint

#Permet de lancer un nombre donné de dés
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