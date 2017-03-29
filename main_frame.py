import random
import scenes
import chars
import weapons
import items
import battle_engine

# What kind of game?

# A detective game with an inventory system

# Aram on the hunt for Shio, in the Lower Districts

battle_engine = battle_engine.BattleEngine()

main_char, npc_pool = chars.choose_char()		

main_char.current_location = main_char.starting_location

main_char.inventory['potion'] = items.HealingPotion()
main_char.inventory['present'] = items.HealingPotion()

while main_char.alive:

	print("You are currently in %s.\n" % main_char.current_location.name)
	print("Choose your next action:\n")

	choice = input("> ")
	
	if 'fight' in choice:
		for char in npc_pool:
			if char in choice:
				enemy = npc_pool[char]
				battle_engine.battle(main_char, enemy, main_char.current_location)
				
	elif 'look around' in choice:
		print(main_char.current_location.description)
		
	elif 'look at' in choice:
		for npc in npc_pool:
			if npc_pool[npc].name in choice.title():
				print(npc_pool[npc].description)
				
	elif 'inventory' in choice:
		items.print_inventory(main_char)

