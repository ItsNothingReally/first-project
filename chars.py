import weapons
import scenes

class Character(object):
	
	alive = True
	weapon = None
	armor = 0
	temporary_armor = 0
	playable = False
	
	def death(self):
		self.alive = False
		print("%s collapses and dies." % self.name)

class Aram(Character):

	def __init__(self):
		
		self.name = "Aram"
		self.max_HP = 30
		self.current_HP = 30
		self.speed = 31
		self.inventory = {}
		self.starting_location = scenes.TheIsland()
	
	description = """
	A Protector from the Horizon wearing the typical emerald uniform. His eyes 
	seem to be constantly scanning his surroundings and his expression leaves 
	little room for any interpretation of his mood.
	"""
	weapon = weapons.Pistol()
	
	
	
	animal = "Tabito"
	
class Francis(Character):

	def __init__(self):
		
		self.name = "Francis"
		self.max_HP = 20
		self.current_HP = 20
		self.speed = 35
		self.inventory = []
		self.starting_location = scenes.TheIsland()
		self.description = """
		Sitting at a table in the corner fiddling around with something in his 
		hands. He seems to be uneasy around large groups of people. Dressed 
		in a black jacket patched up in multiple locations using slogans such 
		as 'Shine On' and 'We Belong Together'.
		""" 
	

	weapon = weapons.Pistol()
	
class Podrey(Character):

	def __init__(self):
		
		self.name = "Podrey"
		self.max_HP = 30
		self.current_HP = 30
		self.speed = 24
		self.inventory = []
		self.starting_location = scenes.Fountain()
		self.description = """
		Constantly fiddling around with something in his hands, seems to be uneasy 
		around large groups of people. Dressed in a black jacket patched up in 
		multiple locations using slogans such as 'Shine On' and 'We Belong Together'.
		"""  
	
class TAR_30(Character):

	def __init__(self):
		
		self.name = "TAR-30"
		self.max_HP = 20
		self.current_HP = 20
		self.speed = 42
		self.inventory = []
		self.starting_location = scenes.Fountain()
		self.description = """
	A shining black orb floating a little over a meter in the air using an 
	advanced propulsion system. Usually, but not always accompanied by a 
	Company engineer. Able to give out commands to humans and feedback to 
	other orbs.
	""" 
		
	weapon = weapons.CuttingLaser()
	
def choose_char():

	character_pool = {
		'aram': Aram(),
		'francis': Francis(),
		'tar-30': TAR_30(),
		'podrey': Podrey()
	}

	print("Choose your character:")
	print("1. Aram\t\t2. Francis\t3. TAR-30\t4. Podrey")

	choice = input("> ")

	main_char = character_pool[choice.lower()]

	main_char.playable = True
	
	npc_pool = {}
	
	for char in character_pool:
		if not character_pool[char].playable:
			npc_pool[char] = character_pool[char]
		
	return main_char, npc_pool