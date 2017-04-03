import random

# locations class file

class Scene(object):

	pass

class Fountain(Scene):

	name = "The Fountain"
	
	description = """
	A fountain.
	"""
	
class TheIsland(Scene):
	
	name = "The Island"
	
	description = """
		The Island is a dimly lit bar where people from all walks of
		life gather to seek refuge from the dreading outside world. The
		owner is widely respected for not discriminating between his customers.
	
		Staff is busy delivering drinks and food, rushing past tables packed
		with customers. Tables here and there hold empty glasses and plates.
	
		Doors leading to the depths of the Island next to the counter are
		accessible only to a select few, and guests regularly joke about
		the kingdom that lies under their feet.
	
		Dancers perform on the stage in the middle of The Island, twisting 
		their bodies like snakes.  The music they are dancing to has taken
		over every corner of the bar and most guests have given up trying
		to have a conversation. Instead, they are watching the dancers
		shake and twirl as if they were possessed.
	
		Aram and Francis are sitting at a table, taking turns to take
		puffs from the steaming tower set up between them.
		"""
	
	
	mid_battle = """
		Tables are flipped and guests are fleeing the scene, hands held
		over their heads. From time to time, the owner of The Island can
		be seen peeking out from behind the counter, only to swear and duck down again.
		"""
	
class TheFactory(Scene):

	name = "The Factory"

	description = """
	A white world filled with conveyor belts and machinery operating like 
	clockwork. Here and there arms are attached to torsos, other places birth
	outlandish contraptions that look more like huge molecules. After every
	step, one more part of them starts moving, until they eventually finish themselves.
	"""