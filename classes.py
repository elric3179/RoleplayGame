#Récupére les attaques disponibles en fonction d'une classe (texte)
#Retourne un tuple qui contient un tuple par attaque sous la forme
#("NomCompetence", mana, num, "Description", ("Type"))
def competences(classe) -> tuple:
    match classe:
        case "berserker":
            return (
                ('Psychotic Style', 8, {'atthp': 10}, 'The berserker loses control, dealing 10 damage'),
                ('Unbreakable Will', 12, {'def': 20}, 'The berserker channels their inner fury, increasing their defense by 20 points'),
                ('Raging Storm', 15, {'atthp': 15}, 'The berserker unleashes a fierce storm of attacks, dealing 15 damage'),
                ('Bloodlust', 30, {'hp': 25, 'atthp': 25}, 'The berserker enters a frenzied state, increasing their health and dealing damage by 25 points'),
            )
        case "mage":
            return (
                ('Fireball', 8, {'atthp': 10}, 'The mage throws a ball of fire, dealing 10 damage'),
                ('Ice Barrier', 12, {'def': 15}, 'The mage creates a barrier of ice, increasing their defense by 15 points'),
                ('Lightning Bolt', 15, {'atthp': 15}, 'The mage calls down a bolt of lightning, dealing 15 damage'),
                ('Mana Drain', 20, {'mana': 20, 'attmana': 20}, 'The mage drains the mana of their opponent, restoring their own mana by 20 points')
            )
        case "paladin":
            return (
                ('Holy Strike', 10, {'atthp': 15}, 'The paladin strikes with holy power, dealing 15 damage'),
                ('Divine Shield', 12, {'def': 20}, 'The paladin calls upon a divine shield, increasing their defense by 20 points'),
                ('Heal', 8, {'hp': 20}, 'The paladin heals themselves for 20 health points'),
                ('Divine Retribution', 20, {'atthp': 25}, 'The paladin unleashes divine retribution, dealing 25 damage')
            )
        case "archer":
            return (
                ('Precise Shot', 8, {'atthp': 10}, 'The archer fires a precise shot, dealing 10 damage'),
                ('Mana Boost', 12, {'mana': 8}, 'The archer boosts their mana by 8 points'),
                ('Evasive Maneuvers', 15, {'def': 20}, 'The archer performs evasive maneuvers, increasing their defense by 20 points'),
                ('Rain of Arrows', 20, {'atthp': 18}, 'The archer calls forth a rain of arrows, dealing 15 damage')
            )
#Recupére les stats de base d'un calsse en fonction du nom de cette classe
#Retourne un dictionnaire sous la forme
#{"mana": NumMana, "hp": NumHp, "def": NumDef, "topMana": NumTopMana}
def stats(classe) -> dict:
    match classe:
        case "berserker":
            return {"class":classe,"mana":0,"hp":100,"def":20,"topMana":40}
        case "mage":
            return {"class":classe,"mana":10,"hp":80,"def":10,"topMana":60}
        case "paladin":
            return {"class":classe,"mana":0,"hp":60,"def":30,"topMana":80}
        case "archer":
            return {"class":classe,"mana": 20, "hp": 75, "def": 15, "topMana": 60}


def show_classe(index:int):
    red     = lambda string: "\033[1;31m" + string + "\033[0;00m"
    classes = get_classes()
    for i in range(len(classes)):
        if index == i:
            print(red("» ") + ": " + str(classes[i]).title())
        else:
            print("» " + ": " + str(classes[i]).title())


def get_classes(num=None):
    classes_name = ("berserker", "mage", "paladin", "archer")
    if num != None:
        return classes_name[num]
    else:
        return classes_name
    