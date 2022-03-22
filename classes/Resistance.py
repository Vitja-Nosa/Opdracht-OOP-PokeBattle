from unicodedata import name

from classes.EnergyType import EnergyType


class Resistance:
    def __init__(self, energyType, value):
        self.energyType = energyType
        self.value = value