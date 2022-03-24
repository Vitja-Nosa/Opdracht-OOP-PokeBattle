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
        for obj in self.attacks:
            if obj.name == attack:
                attack = obj
                break
        if type(attack) == str:
            print('Unknown attack.\n')
            return False
        print(target.name+ " has "+ str(self.health) + " health.")
        print(self.name + " attacks " + target.name + " with " + attack.name + ".")
        target.takeDmg(self.energyType, attack)
    def takeDmg(self, energyType, attack):
        dmg = attack.value
        if (energyType.name == self.weakness.energyType.name):
            dmg *= self.weakness.multiplier
        if (energyType.name == self.resistance.energyType.name):
            dmg -= self.resistance.value
        self.health -= dmg
        print(self.name+ " has "+ str(self.health) + " health.\n")
        if self.health <= 0:
            Pokemon.amount = Pokemon.amount - 1
            print(self.name+' died!')
            Pokemon.list.pop(Pokemon.list.index(self)) # killing the target
        
    @staticmethod
    def getPopulation():
        return Pokemon.amount