import random

# What kind of game?

# A detective game with an inventory system

# Aram on the hunt for Shio, in the Lower Districts

class Battle(object):

	def fazow(self):
		print("fazow!")

	def battle(self, charA, charB):

	# decide who has initiative
	
		if charA.speed > charB.speed:
			first_to_go = charA
			second_to_go = charB
		else:
			first_to_go = charB
			second_to_go = charA

		print("%s goes first." % first_to_go.name)
	
	# battle turn rotation
	
		while charA.alive and charB.alive:
	
			# first to go
		
			print("%s's turn." % first_to_go.name)
		
			self.turn(first_to_go, second_to_go)
			
			# second to go
			if not second_to_go.alive:
				break
			else:
				print("%s's turn." % second_to_go.name)
		
				self.turn(second_to_go, first_to_go)
			
	def turn(self, charA, charB):

		action_point = 1
		charA.temporary_armor = 0
	
		while action_point == 1:
	
			if not charA.playable:
				choice = self.automated()
			else:
				print("1. Attack \t2. Defend\n3. Item \t4. Run\n")
				choice = input(">").lower()
		
			if choice == "attack":
				if charA.weapon == None:
					print("No weapon!")
				else:
					charA.weapon.shoot(charB)
					action_point -= 1
			elif choice == "defend":
				print("%s takes a defensive stance." % charA.name)
				charA.temporary_armor += 2
				print("%s's defense is now %d.\n" % (charA.name, charA.temporary_armor))
				action_point -= 1
			elif choice == "item":
				print("%s's inventory:" % charA.name)
			elif choice == "run":
				print("%s flees from the battle." % charA.name)
				action_point -= 1
				exit(1)
	
	def automated(self):
		choices = ["attack", "defend"]
		return choices[random.randint(0, len(choices) - 1)]
		
def recording(charA, charB, number):
	
	battle_records = {}
	
	battle_records[charA.name] = 0
	battle_records[charB.name] = 0
	
	for i in range(number):
	
		charA.alive = True
		charB.alive = True
	
		crossing_paths.battle(charA, charB)
			
		if not charA.alive:
			battle_records[charA.name] += 1
		else:
			battle_records[charB.name] += 1
			
	winning_percentage_A =  
			
	recording_file = open('battle_record.txt', 'a')
				
	recording_file.write("%s died %i times. %s died %i times.\n" %(charA.name, battle_records[charA.name], charB.name, battle_records[charB.name]))
	
	recording_file.close()

