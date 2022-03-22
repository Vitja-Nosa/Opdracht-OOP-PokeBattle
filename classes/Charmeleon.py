from classes.Pokemon import Pokemon

class Charmeleon(Pokemon):
    def __init__(self, name, maxHealth, energyType, attacks, weakness, resistance):
        super().__init__(name, maxHealth, energyType, attacks, weakness, resistance)