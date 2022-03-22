class Pokemon:
    def __init__(self, name, maxHealth, energyType, attacks, weakness, resistance):
        self.name = name
        self.hitpoints = maxHealth
        self.health = maxHealth
        self.energyType = energyType
        self.attacks = attacks
        self.weakness = weakness
        self.resistance = resistance
    def Attack(self, target):
        dmg = self.attacks.value
        if (self.energyType.name == target.weakness.energyType.name):
            dmg *= target.weakness.multiplier
        if (self.energyType.name == target.resistance.energyType.name):
            dmg -= target.resistance.value
        target.health -= dmg
        
