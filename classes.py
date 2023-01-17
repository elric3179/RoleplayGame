def attacks(classe) -> tuple:
    if classe == "berserker":
        return (
            ("Psychotic Style", 8, 10, "The berserker loses control, dealing 10 damage", ("att")),
            ("Unbreakable Will", 12, 20, "The berserker channels their inner fury, increasing their defense by 20 points", ("def")),
            ("Raging Storm", 15, 15, "The berserker unleashes a fierce storm of attacks, dealing 15 damage", ("att")),
            ("Bloodlust", 30, 25, "The berserker enters a frenzied state, increasing their health and dealing damage by 25 points", ("hp", "att"))
        )
    elif classe == "mage":
        return (
            ("Fireball", 8, 10, "The mage throws a ball of fire, dealing 10 damage", ("att")),
            ("Ice Barrier", 12, 15, "The mage creates a barrier of ice, increasing their defense by 15 points", ("def")),
            ("Lightning Bolt", 15, 15, "The mage calls down a bolt of lightning, dealing 15 damage", ("att")),
            ("Mana Drain", 20, 20, "The mage drains the mana of their opponent, restoring their own mana by 20 points", ("mana","attmana"))
        )

def stats(classe):
    if classe == "berserker":
        return {"mana":0,"hp":100,"def":20,"topMana":40}
    elif classe == "mage":
        return {"mana":10,"hp":80,"def":10,"topMana":80}

berserkers = {"att":attacks("berserker"),"stats":stats("berserker")}
mages = {"att":attacks("mage"),"stats":stats("mage")}
print(berserkers)