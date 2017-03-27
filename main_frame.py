import random

import chars
print("Sending souls through the rift... done!")
import weapons
print("Importing weapons... done!")
import locations
print("Painting stunning vistas... done!")
import battle_engine
print("Listening for screams in agony... done!")

aram = chars.Aram()

tar_30 = chars.TAR_30()

francis = chars.Francis()

crossing_paths = battle_engine.Battle()

crossing_paths.battle(aram, tar_30)


	
for i in range(100):
	recording(aram, tar_30, 100)