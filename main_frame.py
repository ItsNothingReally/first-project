import battle_engine
import chars
import items

# What kind of game?

# A detective game with an inventory system

# Aram on the hunt for Shio, in the Lower Districts

battle_engine = battle_engine.BattleEngine()

main_char = chars.Aram()

main_char.current_location = main_char.starting_location

main_char.inventory['potion'] = items.HealingPotion()
main_char.inventory['present'] = items.HealingPotion()

def free_movement(character, npcs, location):

	while character.alive:

		print("Choose your next action:\n")

		choice = input("> ")
	
		if 'fight' in choice:
			for char in npcs:
				if char in choice:
					enemy = npcs[char]
					battle_engine.battle(character, enemy, character.current_location)
				
		elif 'look around' in choice:
			print(character.current_location.description)
		
		elif 'look at' in choice:
			for npc in npcs:
				if npcs[npc].name in choice.title():
					print(npcs[npc].description)
				
		elif 'inventory' in choice:
			items.print_inventory(character)

#free_movement(main_char, npc_pool, main_char.current_location)