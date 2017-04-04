

class Item(object):
	pass


class HealingPotion(Item):
	
	def __init__(self):
		self.name = "Red Vial"
		self.usable_on_others = True
		
	def use(self, target):
		old_HP = target.current_HP
		target.current_HP += 20
		if target.current_HP > target.max_HP:
			target.current_HP = target.max_HP
		print("%s recovered %d HP." % (target.name, target.current_HP - old_HP))
			
def print_inventory(char):
	
	item_count = {}
	
	for item in char.inventory:
		if not char.inventory[item].name in item_count:
			item_count[char.inventory[item].name] = 1
		else:
			item_count[char.inventory[item].name] += 1
		
	print("%s's inventory:\n" % char.name)
	for item in item_count:
		print("%s x %d" % (item, item_count[item]))
	
	print("\n")