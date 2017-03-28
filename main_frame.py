import random
import scenes
import chars
import weapons
import battle_engine

# What kind of game?

# A detective game with an inventory system

# Aram on the hunt for Shio, in the Lower Districts

battle_engine = battle_engine.BattleEngine()

main_char, npc_pool = chars.choose_char()		




while main_char.alive:

	choice = input("> ")
	
	if 'fight' in choice:
		for char in npc_pool:
			if char in choice:
				enemy = npc_pool[char]
				battle_engine.battle(main_char, enemy)
		

