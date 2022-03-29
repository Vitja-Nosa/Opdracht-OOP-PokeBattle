from classes.EnergyType import EnergyType
from classes.Attack import Attack
from classes.Weakness import Weakness
from classes.Resistance import Resistance
from classes.Pokemon import Pokemon
from classes.Pikachu import Pikachu
from classes.Charmeleon import Charmeleon

lightning = EnergyType('Lightning', 0)

name = 'Yellow Thing'
maxHealth = 60
energyType = lightning
attacks = [Attack('Electric Ring', 50), Attack('Pika Punch', 20)]
weakness = Weakness(EnergyType('Fire', 0), 1.5)
resistance = Resistance(EnergyType('Fighting', 0), 20)

Pokemon.list.append(Pikachu(name, maxHealth, energyType, attacks, weakness, resistance))

name = 'Dragon'
maxHealth = 60
energyType = EnergyType('Fire', 0)
attacks = [Attack('Head Butt', 10), Attack('Flare', 30)]
weakness = Weakness(EnergyType('Water', 0), 2)
resistance = Resistance(lightning, 10)

Pokemon.list.append(Charmeleon(name, maxHealth, energyType, attacks, weakness, resistance))

pokemon1 = Pokemon.find('Yellow Thing')
pokemon2 = Pokemon.find('Dragon')

print("The amount of Pokemons are: "+str(Pokemon.getPopulation()))
print("---------------------------------------------------")
print(pokemon2.name + " has "+ str(pokemon2.health) + " health.")
print(pokemon1.name + " attacks " + pokemon2.name + " with Electric Ring.")
pokemon1.Attack('Electric Ring', pokemon2)
print(pokemon2.name + " has "+ str(pokemon2.health) + " health.")
print("---------------------------------------------------")
print(pokemon1.name + " has "+ str(pokemon1.health) + " health.")
print(pokemon2.name + " attacks " + pokemon1.name + " with Flare.")
pokemon2.Attack('Flare', pokemon1)
print(pokemon1.name + " has "+ str(pokemon1.health) + " health.")
print("---------------------------------------------------")
print(pokemon1.name + " has "+ str(pokemon1.health) + " health.")
print(pokemon2.name + " attacks " + pokemon1.name + " with Flare.")
pokemon2.Attack('Flare', pokemon1)
print(pokemon1.name + " has "+ str(pokemon1.health) + " health.")
print("---------------------------------------------------")
print("The amount of Pokemons are: "+str(Pokemon.getPopulation()))