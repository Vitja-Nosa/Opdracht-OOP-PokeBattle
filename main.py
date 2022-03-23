from classes.EnergyType import EnergyType
from classes.Attack import Attack
from classes.Weakness import Weakness
from classes.Resistance import Resistance
from classes.Pokemon import Pokemon
from classes.Pikachu import Pikachu
from classes.Charmeleon import Charmeleon

name = 'Yellow Thing'
maxHealth = 60
energyType = EnergyType('Lightning', 10)
attacks = [Attack('Electric Ring', 50), Attack('Pika Punch', 20)]
weakness = Weakness(EnergyType('Fire', 0), 1.5)
resistance = Resistance(EnergyType('Fighting', 0), 20)

Pokemon.list.append(Pikachu(name, maxHealth, energyType, attacks, weakness, resistance))

name = 'Dragon'
maxHealth = 60
energyType = EnergyType('Fire', 0)
attacks = [Attack('Head Butt', 10), Attack('Flare', 30)]
weakness = Weakness(EnergyType('Water', 0), 2)
resistance = Resistance(EnergyType('Lightning', 10), 10)

Pokemon.list.append(Charmeleon(name, maxHealth, energyType, attacks, weakness, resistance))

Pokemon.list[0].Attack(0, Pokemon.list[1])
Pokemon.list[1].Attack(1, Pokemon.list[0])
Pokemon.list[1].Attack(1, Pokemon.list[0])
