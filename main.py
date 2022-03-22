from classes.EnergyType import EnergyType
from classes.Attack import Attack
from classes.Weakness import Weakness
from classes.Resistance import Resistance
from classes.Pikachu import Pikachu
from classes.Charmeleon import Charmeleon

name = 'dragon'
maxHealth = 60
energyType = EnergyType('Fire', 10)
attacks = Attack('Head Butt', 10)
weakness = Weakness(EnergyType('Water', 10), 2)
resistance = Resistance(EnergyType('Lightning', 10), 10)

pokemon1 = Charmeleon(name, maxHealth, energyType, attacks, weakness, resistance)

name = 'electric rat'
maxHealth = 60
energyType = EnergyType('Lightning', 10)
attacks = Attack('Electric Ring', 50)
weakness = Weakness(EnergyType('Fire', 10), 1.5)
resistance = Resistance(EnergyType('Fighting', 10), 20)

pokemon2 = Pikachu(name, maxHealth, energyType, attacks, weakness, resistance)

pokemon1.Attack(pokemon2)

print(pokemon2.health)