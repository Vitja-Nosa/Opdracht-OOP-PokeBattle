from classes.Pokemon import Pokemon

class Pikachu(Pokemon):
    def __init__(self, name, maxHealth, energyType, attacks, weakness, resistance):
        super().__init__(name, maxHealth, energyType, attacks, weakness, resistance)
        self.__secret = 'this shouldnt be showed'
