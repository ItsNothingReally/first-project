

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
		self.inventory = []
	
	description = """
	A Protector from the Horizon wearing the typical emerald 
	uniform. His eyes seem to be constantly scanning his 
	surroundings and his expression leaves little room for 
	any interpretation of his mood.
	"""
	
	playable = True
	
	animal = "Tabito"
	
class Francis(Character):

	def __init__(self):
		
		self.name = "Francis"
		self.max_HP = 20
		self.current_HP = 20
		self.speed = 35
		self.inventory = []
	
	description = """
	Sitting at a table in the corner fiddling around with
	something in his hands. He seems to be uneasy around 
	large groups of people. Dressed in a black jacket 
	patched up in multiple locations using slogans such 
	as 'Shine On' and 'We Belong Together'.
	""" 

class Podrey(Character):

	def __init__(self):
		
		self.name = "Podrey"
		self.max_HP = 30
		self.current_HP = 30
		self.speed = 24
		self.inventory = []
	
	description = """
	Constantly fiddling around with something in his hands,
	seems to be uneasy around large groups of people.
	Dressed in a black jacket patched up in multiple locations
	using slogans such as 'Shine On' and 'We Belong Together'.
	"""  
	
class TAR_30(Character):

	def __init__(self):
		
		self.name = "TAR-30"
		self.max_HP = 20
		self.current_HP = 20
		self.speed = 42
		self.inventory = []
	
		self.description = """
	A shining black orb floating a little over a meter in the air
	using advanced an advanced propulsion system. Usually, but not
	always accompanied by a Company engineer. Able to give out
	commands to humans and feedback to other orbs.
	"""  