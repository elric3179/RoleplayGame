from random import randint

#Stocke les différentes statistiques de chaque sous la forme:
# "nom": [MaxMana, def]
Classes =  {"none" : [50, 10]}

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


def competence(number, player, competence_type):
    match competence_type:
        case "att":
            print("test")
        case "def":
            print(2)
