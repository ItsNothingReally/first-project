import random


class Weapon(object):

	def __init__(self, min_damage, max_damage):
		self.min_damage = min_damage
		self.max_damage = max_damage
	
	def atk_power(self):
		return random.randint(self.min_damage, self.max_damage)
		
	def hit(self):
		return random.randint(0, 100) < self.accuracy
		
	def shoot(self, target):
	
		if not self.hit():
			print("%s! The shot misses." % self.sound[random.randint(0,len(self.sound)-1)])
		else:
			current_HP = target.current_HP
			damage = self.atk_power() - target.armor
			if damage < 0:
				damge = 0
			target.current_HP -= damage
			print("%s! %s is hit for %d damage!\n" % 
				(self.sound[random.randint(0,len(self.sound)-1)],target.name, damage))
			if target.current_HP <= 0:
				target.death()
			self.clip -= 1

class Melee(Weapon):

	pass
	
class Knife(Melee):

	pass
	
	
class Firearm(Weapon):
		
	def __init__(self, min_damage, max_damage, clip):
		self.min_damage = min_damage
		self.max_damage = max_damage
		self.clip = clip
		self.sound = ["BLAM", "BANG"]
		self.accuracy = 90
				
class Pistol(Firearm):

	pass

class CuttingLaser(Firearm):

	def __init__(self):
		self.min_damage = 3
		self.max_damage = 9
		self.accuracy = 80
		self.clip = 5
		self.sound = ["ZAAPP", "FPSHH"]