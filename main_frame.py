import random
import chars
import weapons
import battle_engine

# What kind of game?

# A detective game with an inventory system

# Aram on the hunt for Shio, in the Lower Districts

aram = chars.Aram()

francis = chars.Francis()

podrey = chars.Podrey()

tar_30 = chars.TAR_30()

gun = weapons.Firearm(4, 6, 6)

laser = weapons.CuttingLaser()

tar_30.weapon = laser

aram.weapon = gun

francis.weapon = laser

battle_engine = battle_engine.BattleEngine()

battle_engine.battle(aram, francis)

if aram.alive:

	print("Proceed to next battle?")
	next_battle = input("> ")
	
	if next_battle == "yes":
		battle(aram, tar_30)
	else:
		print("Farewell.")