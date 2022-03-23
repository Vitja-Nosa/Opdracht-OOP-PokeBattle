class Pokemon:
    list = []
    amount = 0
    def __init__(self, name, maxHealth, energyType, attacks, weakness, resistance):
        Pokemon.amount = Pokemon.amount + 1
        self.name = name
        self.hitpoints = maxHealth
        self.health = maxHealth
        self.energyType = energyType
        self.attacks = attacks
        self.weakness = weakness
        self.resistance = resistance
    def Attack(self, attack, target):
        print(target.name+ " has "+ str(target.health) + " health.")
        print(self.name + " attacks " + target.name + " with " + self.attacks[attack].name + ".")
        dmg = self.attacks[attack].value
        if (self.energyType.name == target.weakness.energyType.name):
            dmg *= target.weakness.multiplier
        if (self.energyType.name == target.resistance.energyType.name):
            dmg -= target.resistance.value
        target.health -= dmg
        print(target.name+ " has "+ str(target.health) + " health.\n")
        if target.health <= 0:
            Pokemon.amount = Pokemon.amount - 1
            print(target.name+' died!')
            Pokemon.list.pop(Pokemon.list.index(target)) # killing the target
    @staticmethod
    def getPopulation():
        return Pokemon.amount