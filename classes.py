#("NomCompetence", mana, num, "Description", ("Type"))
def competences(classe) -> tuple[tuple]:
    """Récupère les compétences disponible ne fonction d'une classe

    """
    match classe:
        case "berserker":
            return (
                ('Psychotic Style', 8, {'atthp': 10}, 'The berserker loses control, dealing value0 damage'),
                ('Unbreakable Will', 12, {'def': 20}, 'The berserker channels their inner fury, increasing their defense by value0 points'),
                ('Raging Storm', 15, {'atthp': 15}, 'The berserker unleashes a fierce storm of attacks, dealing value0 damage'),
                ('Bloodlust', 30, {'hp': 25, 'atthp': 25}, 'The berserker enters a frenzied state, increasing their health and dealing damage by value0 points'),
            )
        case "mage":
            return (
                ('Fireball', 8, {'atthp': 10}, 'The mage throws a ball of fire, dealing value0 damage'),
                ('Ice Barrier', 12, {'def': 15}, 'The mage creates a barrier of ice, increasing their defense by value0 points'),
                ('Lightning Bolt', 15, {'atthp': 15}, 'The mage calls down a bolt of lightning, dealing value0 damage'),
                ('Mana Drain', 20, {'hp': 20, 'attmana': 20}, 'The mage drains value1 mana of their opponent, restoring their own health by value0 points')
            )
        case "paladin":
            return (
                ('Holy Strike', 10, {'atthp': 15}, 'The paladin strikes with holy power, dealing value0 damage'),
                ('Divine Shield', 12, {'def': 20}, 'The paladin calls upon a divine shield, increasing their defense by value0 points'),
                ('Heal', 8, {'hp': 20}, 'The paladin heals themselves for value0 health points'),
                ('Divine Retribution', 20, {'atthp': 25}, 'The paladin unleashes divine retribution, dealing value0 damage')
            )
        case "archer":
            return (
                ('Precise Shot', 8, {'atthp': 10}, 'The archer fires a precise shot, dealing value0 damage'),
                ('Mana Boost', 12, {'mana': 8}, 'The archer boosts their mana by value0 points'),
                ('Evasive Maneuvers', 15, {'def': 20}, 'The archer performs evasive maneuvers, increasing their defense by value0 points'),
                ('Rain of Arrows', 20, {'atthp': 18}, 'The archer calls forth a rain of arrows, dealing value0 damage')
            )

#{"mana": NumMana, "hp": NumHp, "def": NumDef, "topMana": NumTopMana}
def stats(classe) -> dict:
    """Récupére les statistique d'une classe
    """
    match classe:
        case "berserker":
            return {"class":classe,"mana":0,"hp":100,"def":20,"topMana":40,"attacks":competences(classe)}
        case "mage":
            return {"class":classe,"mana":10,"hp":80,"def":10,"topMana":60,"attacks":competences(classe)}
        case "paladin":
            return {"class":classe,"mana":0,"hp":60,"def":30,"topMana":80,"attacks":competences(classe)}
        case "archer":
            return {"class":classe,"mana":20,"hp":75,"def":15,"topMana":60,"attacks":competences(classe)}


def show_classe(index:int):
    """Affiche les classes disponibles
    """
    red     = lambda string: "\033[1;31m" + string + "\033[0;00m"
    classes = get_classes()
    for i in range(len(classes)):
        if index == i:
            print(red("» ") + ": " + str(classes[i]).title())
        else:
            print("» " + ": " + str(classes[i]).title())


def get_classes(num=None):
    """Récupére le nom de la classe grace au nombre qu'il la représente
    """
    classes_name = ("berserker", "mage", "paladin", "archer")
    if num != None:
        return classes_name[num]
    else:
        return classes_name
    