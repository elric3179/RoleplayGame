from random import randint
from classes import *
from math import ceil
from time import sleep
from msvcrt import getch, kbhit
import os,sys

# ------------------------- Mapping des couleurs --------------------------
red         = lambda string: "\033[1;31m" + string + "\033[0;00m"
green       = lambda string: "\033[1;32m" + string + "\033[0;00m"
darkgreen       = lambda string: "\033[0;32m" + string + "\033[0;00m"

# -------------------------- Gestion des stats ----------------------------

attackerStatsList = ["mana","hp","def"]
defenderStatsList = ["atthp","attmana"]

#Permet de déterminer l'éfficacité en fonction de la défense
defenseCalculator = lambda attack, defense : attack / (1+(defense/100))

# --------------------------- Lancement de dés -----------------------------

def roll_dice(dice_number: int) -> list:
    """Lance un certain nombre de dés

    @param dice_number: nombre de dés à lancer
    @rtype: list
    @returns: Liste de résultat de dé
    """
    result = []
    for i in range(dice_number):
        result.append(dice())
    return result


def dice():
    """Lance un dé de 6
    
    @rtype: int
    """
    return randint(1, 6)

def mana(players_stats:list, actual_player:int): 
    """Lancement du dés de mana, ajout du résultat au mana du joueur et affichage de cet ajout
    """
    roll = mana_roll()
    players_stats[0]["mana"] = min(players_stats[0]["topMana"],players_stats[0]["mana"] + roll[0])
    interface(players_stats, actual_player, roll[1])
    sleep(2)

def mana_roll():
    """Lancement des dés de mana et affichage du résultat

    @returns: résultat des dés et string a afficher 
    """
    dice_result = roll_dice(2)
    total = sum(dice_result)
    string_output = f"Lancement de dés de mana... \nVous avez obtenu {dice_result[0]} et {dice_result[1]} pour un total de {total}"
    return (total, (string_output))



# --------------------------- Gestion des classes ---------------------------


def ask_classe():
    """Gére le choix de classe d'un utilisateur

    @rtype: int
    @returns: Entier de 0 à 3 représentant une classe
    """
    sys.stdout.flush()
    classIndex = 0 # Placement du curseur actuelle
    while True:
        os.system("cls"), # Supprime le contenu de l'inteface
        show_classe(classIndex)
        choix = scroll_selection(classIndex, 3) #Selection de la classe grace au flèche directionnelle
        classIndex = choix[0]
        if choix[1] == True:
            break
        
    return int(classIndex)



def classes_selection():
    """Gère la sélection des classes pour les deux joueurs

    @rtype: list
    @returns: liste de deux valeurs de 0 à 3 représentant les classes choisi
    """
    choose_class = [ask_classe() for i in range(2)]
    
    return choose_class


def start_stat() -> list:
    """Crée les statistique de base des 2 joueurs en fonction de leur choix de classe

    @rtype: list
    @returns: liste des statistiques (sous forme de dictionnaire)
    """
    choosen_class = classes_selection()
    players_stats_start = []
    for i in range(len(choosen_class)):
        players_stats_start.append(stats(get_classes(choosen_class[i])))
    return players_stats_start

# ----------------------------- Competence ----------------------------------


def skillRoll(attack:tuple[str,int,dict,str], attackerStats:dict, defenderStats:dict, actual_player):
    """Modifie les statistique des 2 joueurs en fonction d'une compétence

    """
    efficacity = efficacite(5, [attackerStats,defenderStats], actual_player)
    #roll = rollAndDisplayDice([attackerStats,defenderStats],actual_player)
    for i in attack[2].keys():
        if i in defenderStatsList:
            defenderStats[i[3:]] = max(0,defenderStats[i[3:]]-ceil(defenseCalculator(attack[2][i]*efficacity,defenderStats["def"])))
        elif i in attackerStatsList:
            if i == "mana":
                attackerStats[i] = min(attackerStats["topMana"],attackerStats[i] + attack[2][i])
            else:
                attackerStats[i] += int(attack[2][i]*efficacity)

    return [attackerStats, defenderStats]


# ----------------------------- Utilitaire ----------------------------------


def spaceBetween(leftText:str, rightText:str) -> str:
    """Crée un texte au dimension de la fenetre en fonction de deux textes

    @rtype: str
    """
    columnsConst = os.get_terminal_size().columns - len(leftText+rightText)
    return columnsConst


def center(string: str) -> str:
    """Centre un texte sur le centre de la fenetre

    @rtype: str
    @returns: texte centré
    """
    return int(((os.get_terminal_size().columns / 2) - (len(string) / 2)))*" " + string


def player_menu(player_stat:dict, player_number:int) -> str:
    """Crée un texte de présentation des statistiques d'un personnages

    @param player_stat: statistique d'un joueur
    @rtype: str
    @returns: texte formatté avec les statiques d'un joueur
    """
    text_result = []

    text_result.append("╭" +20*"─" + "╮")
    text_result.append(("│ " + "Joueur " + str(player_number + 1) + 11*" " +  "│" ))
    text_result.append(("│ " + "Classe: " + f"{player_stat['class'].title():<11}" + "│"))
    text_result.append(("│ " +"Mana: "+ f"{player_stat['mana']:<2}"+ " HP: "+ f"{player_stat['hp']:<3}"  + 3*" "+ "│"))
    text_result.append("╰" +20*"─" + "╯")

    return text_result



def chooseFirstPlayer(players_stat: list) -> list:
    """Choisi le premier joueur et affiche le choix avec une animation

    @rtype: int
    @returns: nombre réprésentant le premier joueur (0 ou 1)
    """
    for i in range(9):
        os.system("cls")
        dots = "."*(i%3+1)
        displayCustomMessage(f"Choosing first player{dots:<3}")
        sleep(0.3)
    choosen = randint(0,1)
    if choosen == 1:
        players_stat.reverse()

    sayWhoIsFirst(choosen+1)
    return choosen

def sayWhoIsFirst(number:int):
    """Affiche le joueur choisi
    """
    os.system("cls")
    displayCustomMessage(f"Le premier joueur est le numéro {number}")


def displayCustomMessage(message:str):
    """Affiche un message dans un format défini pour l'affichage (centré et encadré)
    """
    
    split_message = message.split("\n") #Permet l'affichage multiligne
    max_len = len(max(split_message, key=len)) #Trouve le nombre maximum de caractère dans une ligne
    
    print(center(("╭" + (max_len)*"─" + "╮")))

    for i in range(len(split_message)):
        text = "".join(("│", split_message[i], (max_len - len(split_message[i]))*" " ,"│"))
        print(center(text))

    print(center("╰" + (max_len)*"─" + "╯"))

def interface(players_stat:list, actual_player:int, message:str):
    """Affiche l'interface de jeu avec les statistiques des 2 joueurs et un message
    """
    os.system("cls")

    other_player = actual_player ^1
    actual_message = [i for i in player_menu(players_stat[0], actual_player)]
    
    index = 0
    for i in player_menu(players_stat[1], other_player):
        actual_message[index] += spaceBetween(actual_message[index],i)*" " + i
        index += 1

    for i in actual_message:
        print(green(i[:28]) + red(i[28:]))

    print(2*"\n")
    displayCustomMessage(message)


def scroll_selection(index:int, maxValeur:int):
    """Gère une sélection par flèche et entrée

    @param index: placement du curseur
    @param maxValeur: valeur maximale
    @returns: index mis a jour et booléen en fonction de l'appuie de entrée
    """
    char = getch() #Récupére la dernière touche du clavier
    match char:
        case b"P":
            index = min(maxValeur,index+1)
        case b"H":
            index = max(0,index-1)
        case b"\n" | b"\r" | b"\r\n" | b"\n\r":
            return index, True
    return index, False

def display_competence(player_stats: dict, competenceIndex: int) -> str:
    """Crée le texte de présentation des différentes compétences d'un joueur 
    """
    comp = player_stats["attacks"]
    display_text = "Competences:"
    for i in range(len(comp)):
        if i == competenceIndex:
            display_text += f"\n>: {comp[i][0]}, {convertValueInString(comp[i][3], comp[i])} ;  {comp[i][1]} mana"
        else:
            display_text += f"\n█: {comp[i][0]}, {convertValueInString(comp[i][3], comp[i])} ;  {comp[i][1]} mana"
    display_text += f"\n{'>' if competenceIndex == 4 else '█'}: Keep the mana"
    return display_text

def convertValueInString(string:str, competence:dict) -> str:
    """Affichage dynamique des statistiques dans les compétences

    @returns: string modifié avec les bonnes valeurs
    """
    for i in range(len(competence[2].keys())):
        string = string.replace(f"value{i}", str(competence[2][list(competence[2].keys())[i]]))
    return string



# --------------------------------- Autre -----------------------------------


def game_loop(players_stats:list):
    """Gère les tours de chaque joueur
    """
    actual_player = chooseFirstPlayer(players_stats)
    
    sleep(2)
    while True:
        players_stats = turn(actual_player, players_stats)
        if(players_stats[1]["hp"] == 0): # Victoire
            print("Joueur " + str(actual_player + 1) + " a gagné") 
            break
        actual_player ^= 1
        players_stats.reverse()



def turn(actual_player, players_stats):
    """Gère le déroulement d'un tour
    """

    mana(players_stats, actual_player) 

    competence = choose_competence(actual_player, players_stats)
    return skillRoll(competence, players_stats[0], players_stats[1],actual_player)

def choose_competence(actual_player, players_stats):
    """Choix d'un compétence

    @returns: compétence choisi
    """
    competence = None
    while competence == None:
        competenceIndex = 0
        os.system("cls")
        while kbhit():
            getch()
        interface(players_stats, actual_player, display_competence(players_stats[0], competenceIndex))
        while True:

            interface(players_stats, actual_player, display_competence(players_stats[0], competenceIndex))
            choix = scroll_selection(competenceIndex, 4)
            competenceIndex = choix[0]
            if choix[1] == True:
                break
            
        if competenceIndex == None:
            pass
        elif competenceIndex == 4:
            # Pour ne pas rentrer dans une erreur avec le fait de garder le mana
            return players_stats
        elif players_stats[0]["attacks"][competenceIndex][1] > players_stats[0]["mana"]:
            interface(players_stats,actual_player,"You do not have enough mana!")
            competence = None
            sleep(2)
        else:
            players_stats[0]["mana"] -= players_stats[0]["attacks"][competenceIndex][1]
            return players_stats[0]["attacks"][competenceIndex]

    

def play():
    """Lancement du jeu
    """
    players_stats = start_stat()
    game_loop(players_stats)


def efficacite(dice_number: int, players_stats: list, actual_player: int) -> int:
    """Détermine le pourcentage d'éfficacité de la compétence en fonction d'une mécanique qui demande au joueur de réorganiser des résultats de dés pour se rapprocher d'un nombre donné
    """
    numberToReach = roll_dice(dice_number)
    numberGet = roll_dice(dice_number)
    
    index = 0
    selected = -1
    while True:
        
        string = ""
        string += "Try to reach " + ("".join(map(str, numberToReach))) + " after press the backspace key"+ "\n"
        
        for i in range(len(numberGet)):
            if index == i:
                string += ">"
            else:
                string += " "
            string += str(numberGet[i])

        os.system("cls")
        interface(players_stats,actual_player,string)

        char = getch()
        match char:
            case b"M":
                index = min(dice_number - 1,index+1)
                if selected != -1:
                    numberGet.insert(min(dice_number, selected + 2) , numberGet[selected])
                    del numberGet[selected]
                    selected = index
            case b"K":
                index = max(0,index-1)
                if selected != -1:
                    numberGet.insert(max(0, selected - 1) , numberGet[selected])
                    del numberGet[selected + 1]
                    selected = index
            case b"\n" | b"\r" | b"\r\n" | b"\n\r":
                if selected == -1:
                    selected = index
                else:
                    selected = -1
            case b'\x08':
                break
                
    difference = abs(int("".join(map(str, numberToReach))) - int("".join(map(str, numberGet))))
    if numberGet == numberToReach:
        return 1.25
    elif difference < 100:
        return 1.1
    elif difference < 500:
        return 1
    elif difference < 1500:
        return 0.8
    else:
        return 0.6

play()
